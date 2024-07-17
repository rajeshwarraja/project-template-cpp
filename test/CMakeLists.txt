find_package(GTest REQUIRED)

file(GLOB TEST_SRC_FILES RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} src/*.cpp)

add_executable(${PROJECT_NAME}.Test ${TEST_SRC_FILES})
target_link_libraries(${PROJECT_NAME}.Test PRIVATE ${PROJECT_NAME} gtest::gtest)

include(GoogleTest)
gtest_discover_tests(${PROJECT_NAME}.Test)