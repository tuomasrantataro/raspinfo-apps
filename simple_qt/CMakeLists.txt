cmake_minimum_required(VERSION 3.14.0)
project( simple_qt
         VERSION 0.1.0
         DESCRIPTION "Simple app to test that qt has been deployed succesfully"
         HOMEPAGE_URL "https://github.com/tuomasrantataro/raspinfo-apps"
         LANGUAGES CXX )

# For Qt
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)   

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_compile_definitions(
    $<$<CONFIG:Release>:QT_NO_DEBUG_OUTPUT>)

find_package(Qt5 COMPONENTS Core REQUIRED)

add_compile_options(-Wall)

add_executable(simple_qt 
    app.cpp
    main.cpp)

target_link_libraries(simple_qt
                Qt5::Core
)
