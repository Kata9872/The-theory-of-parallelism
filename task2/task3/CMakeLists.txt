cmake_minimum_required(VERSION 3.10)
project(Task3)

set(CMAKE_CXX_STANDARD 11)

find_package(OpenMP REQUIRED)

add_executable(task3_1 task3_1.cpp)
target_link_libraries(task3_1 OpenMP::OpenMP_CXX)
target_compile_options(task3_1 PRIVATE -O3 -Wall)

add_executable(task3_2 task3_2.cpp)
target_link_libraries(task3_2 OpenMP::OpenMP_CXX)
target_compile_options(task3_2 PRIVATE -O3 -Wall)