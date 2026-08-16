function(biomeche_q0_link_opennurbs target)
    set(BIOMECHE_OPENNURBS_ROOT "" CACHE PATH "Path to pinned openNURBS source tree")
    if(NOT BIOMECHE_OPENNURBS_ROOT)
        message(FATAL_ERROR "Set -DBIOMECHE_OPENNURBS_ROOT=/path/to/opennurbs")
    endif()
    if(NOT EXISTS "${BIOMECHE_OPENNURBS_ROOT}/CMakeLists.txt")
        message(FATAL_ERROR "openNURBS CMakeLists.txt not found at ${BIOMECHE_OPENNURBS_ROOT}")
    endif()

    # Q0 consumes the upstream public static target and keeps its object model
    # behind the product-owned adapter. No Rhino SDK / Rhino process is required.
    set(BUILD_TESTING OFF CACHE BOOL "" FORCE)

    add_subdirectory(
        "${BIOMECHE_OPENNURBS_ROOT}"
        "${CMAKE_BINARY_DIR}/_deps/opennurbs"
        EXCLUDE_FROM_ALL
    )

    if(NOT TARGET opennurbsStatic)
        message(FATAL_ERROR "Expected openNURBS target opennurbsStatic was not created")
    endif()

    target_include_directories(${target} PRIVATE "${BIOMECHE_OPENNURBS_ROOT}")
    target_link_libraries(${target} PRIVATE opennurbsStatic)
endfunction()
