cmake_minimum_required (VERSION 2.6)
project(mhaToNii)

FIND_PACKAGE ( ITK REQUIRED)
INCLUDE( ${ITK_USE_FILE} )

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${PROJECT_SOURCE_DIR}/cmake)

#include_directories( include )

add_subdirectory (src)



