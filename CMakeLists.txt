cmake_minimum_required(VERSION 3.10)
project(Jishcord, VERSION 0.1)

if(UNIX)
    message("UNIX system detected")
elseif(WIN32)
    message("WIN32 system detected")
endif()

if (${CMAKE_SYSTEM_NAME} MATCHES Darwin)
    message("MAC OS system detected")
elseif (${CMAKE_SYSTEM_NAME} MATCHES Windows)
    message("WIN system detected")
endif()

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
message("Cpp standart ${CMAKE_CXX_STANDARD}")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")

add_executable(jish main.cpp)