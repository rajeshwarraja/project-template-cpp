file(GLOB LIB_SRC_FILES RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} src/*.cpp)

add_library(${PROJECT_NAME}.Library ${LIB_SRC_FILES})
target_include_directories(${PROJECT_NAME}.Library PUBLIC include)