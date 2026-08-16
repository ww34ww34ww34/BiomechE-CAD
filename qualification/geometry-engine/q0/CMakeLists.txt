cmake_minimum_required(VERSION 3.20)

project(BiomechEGeometryQ0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(BIOMECHE_Q0_CANDIDATE "" CACHE STRING "Geometry candidate: opensubdiv or opennurbs")
set_property(CACHE BIOMECHE_Q0_CANDIDATE PROPERTY STRINGS opensubdiv opennurbs)

if(NOT BIOMECHE_Q0_CANDIDATE)
    message(FATAL_ERROR "Set -DBIOMECHE_Q0_CANDIDATE=opensubdiv|opennurbs")
endif()

add_executable(biomeche_geometry_q0_smoke
    src/main.cpp
)

target_include_directories(biomeche_geometry_q0_smoke PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

if(MSVC)
    target_compile_options(biomeche_geometry_q0_smoke PRIVATE /W4 /permissive- /EHsc)
else()
    target_compile_options(biomeche_geometry_q0_smoke PRIVATE -Wall -Wextra -Wpedantic)
endif()

if(BIOMECHE_Q0_CANDIDATE STREQUAL "opensubdiv")
    include(cmake/CandidateOpenSubdiv.cmake)
    target_sources(biomeche_geometry_q0_smoke PRIVATE src/candidate_opensubdiv.cpp)
    biomeche_q0_link_opensubdiv(biomeche_geometry_q0_smoke)
elseif(BIOMECHE_Q0_CANDIDATE STREQUAL "opennurbs")
    include(cmake/CandidateOpenNurbs.cmake)
    target_sources(biomeche_geometry_q0_smoke PRIVATE src/candidate_opennurbs.cpp)
    biomeche_q0_link_opennurbs(biomeche_geometry_q0_smoke)
else()
    message(FATAL_ERROR "Unknown BIOMECHE_Q0_CANDIDATE='${BIOMECHE_Q0_CANDIDATE}'")
endif()

if(EMSCRIPTEN)
    set_target_properties(biomeche_geometry_q0_smoke PROPERTIES SUFFIX ".js")
    target_link_options(biomeche_geometry_q0_smoke PRIVATE
        "-sENVIRONMENT=node,web"
        "-sEXIT_RUNTIME=1"
        "-sASSERTIONS=0"
    )
endif()

message(STATUS "BiomechE Q0 candidate: ${BIOMECHE_Q0_CANDIDATE}")
message(STATUS "C++ standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "Emscripten: ${EMSCRIPTEN}")
