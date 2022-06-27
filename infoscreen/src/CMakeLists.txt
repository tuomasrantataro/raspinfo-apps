set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOMOC ON)  
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt5 COMPONENTS Core Sql Gui Quick REQUIRED)

add_executable(InfoScreen
    main.cpp
    dbaccess.cpp
    listmodel.cpp
    InfoScreen.qrc
)
target_link_libraries(InfoScreen
    Qt5::Core
    Qt5::Sql
    Qt5::Gui
    Qt5::Quick 
)

install(TARGETS InfoScreen
    RUNTIME
        DESTINATION bin
)