import QtQuick 2.12
import QtQuick.Controls 2.12

import "./components"

import "." as App

ApplicationWindow {
    id: window
    width: 1024
    height: 768
    visible: true
    title: "InfoScreen"

    Rectangle {
        width: parent.width
        height: parent.height
        layer.enabled: true

        color: "green"

        ListView {
            id: listView
            anchors.fill: parent
            anchors.margins: 5

            model: listmodel

            delegate: EventDelegate {}
        }
    }

    Rectangle {
        width: parent.width
        height: parent.height
        layer.enabled: true

        visible: false

        opacity: 0.8
        color: "plum"
    }

}