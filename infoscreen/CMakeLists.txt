cmake_minimum_required(VERSION 3.14.0)
project( InfoScreen
         VERSION 0.1.0
         DESCRIPTION "Event information display app with calendar events and fullscreen adverts"
         HOMEPAGE_URL "https://github.com/tuomasrantataro/raspinfo-apps"
         LANGUAGES CXX )

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR})

add_subdirectory(src)

#add_subdirectory(test)

install(
    TARGETS ${PROJECT_NAME}
    RUNTIME
        DESTINATION bin
        COMPONENT runtime
)