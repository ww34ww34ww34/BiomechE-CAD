function(biomeche_q0_link_opensubdiv target)
    set(BIOMECHE_OPENSUBDIV_ROOT "" CACHE PATH "Path to pinned OpenSubdiv v3_7_0 source tree")
    if(NOT BIOMECHE_OPENSUBDIV_ROOT)
        message(FATAL_ERROR "Set -DBIOMECHE_OPENSUBDIV_ROOT=/path/to/OpenSubdiv")
    endif()
    if(NOT EXISTS "${BIOMECHE_OPENSUBDIV_ROOT}/CMakeLists.txt")
        message(FATAL_ERROR "OpenSubdiv CMakeLists.txt not found at ${BIOMECHE_OPENSUBDIV_ROOT}")
    endif()

    # Q0 needs only the headless CPU/core path. Disable optional render/example stacks.
    set(NO_EXAMPLES ON CACHE BOOL "" FORCE)
    set(NO_TUTORIALS ON CACHE BOOL "" FORCE)
    set(NO_REGRESSION ON CACHE BOOL "" FORCE)
    set(NO_PTEX ON CACHE BOOL "" FORCE)
    set(NO_DOC ON CACHE BOOL "" FORCE)
    set(NO_OMP ON CACHE BOOL "" FORCE)
    set(NO_TBB ON CACHE BOOL "" FORCE)
    set(NO_CUDA ON CACHE BOOL "" FORCE)
    set(NO_OPENCL ON CACHE BOOL "" FORCE)
    set(NO_CLEW ON CACHE BOOL "" FORCE)
    set(NO_OPENGL ON CACHE BOOL "" FORCE)
    set(NO_METAL ON CACHE BOOL "" FORCE)
    set(BUILD_SHARED_LIBS OFF CACHE BOOL "" FORCE)

    add_subdirectory(
        "${BIOMECHE_OPENSUBDIV_ROOT}"
        "${CMAKE_BINARY_DIR}/_deps/opensubdiv"
        EXCLUDE_FROM_ALL
    )

    if(NOT TARGET osd_static_cpu)
        message(FATAL_ERROR "Expected OpenSubdiv target osd_static_cpu was not created")
    endif()

    target_include_directories(${target} PRIVATE "${BIOMECHE_OPENSUBDIV_ROOT}")
    target_link_libraries(${target} PRIVATE osd_static_cpu)
endfunction()
