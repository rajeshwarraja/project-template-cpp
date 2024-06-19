include(FetchContent)

FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        v1.14.0)

set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

file(GLOB TEST_SRC_FILES RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} src/*.cpp)

add_executable(${PROJECT_NAME}.Test ${TEST_SRC_FILES})
target_link_libraries(${PROJECT_NAME}.Test PRIVATE ${PROJECT_NAME}.Library gtest_main)

include(GoogleTest)
gtest_discover_tests(${PROJECT_NAME}.Test)