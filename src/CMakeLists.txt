add_executable(${PROJECT_NAME}
    main.cpp
    clipper2.hpp
    double2.hpp
    double3.hpp
)
target_link_libraries(${PROJECT_NAME}
    nlohmann_json::nlohmann_json
)
if(VCPKG_TARGET_TRIPLET)
    # vcpkg
    target_link_libraries(${PROJECT_NAME}
        PkgConfig::Clipper2
    )
else()
    # conan
    target_link_libraries(${PROJECT_NAME}
        clipper2::clipper2
    )
endif()

# install
install(TARGETS ${PROJECT_NAME}
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
)
