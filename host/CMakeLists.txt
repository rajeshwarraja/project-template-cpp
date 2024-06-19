file(GLOB HOST_SRC_FILES RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} src/*.cpp)

add_executable(${PROJECT_NAME}.Host ${HOST_SRC_FILES})
target_link_libraries(${PROJECT_NAME}.Host PRIVATE ${PROJECT_NAME}.Library)