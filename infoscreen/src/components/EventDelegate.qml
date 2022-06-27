import QtQuick 2.12
import "formDateString.js" as DateScript

Component {
    id: eventDelegate

    Rectangle {
        id: container
        width: listView.width
        height: listView.height/4
        border.color: "green"
        border.width: 5
        Item {
            id: texts
            anchors.fill: container
            Text {
                id: text_summary
                anchors.top: texts.top
                topPadding: 5
                leftPadding: 25
                rightPadding: 25
                text: summary
                font.pointSize: (container.height-15)/3
                font.capitalization: Font.AllUppercase
                font.weight: Font.DemiBold
                color: "black"
                maximumLineCount: 1
                elide: Text.ElideRight 
                width: listView.width
            }
            Text {
                id: text_timestring
                anchors.top: text_summary.bottom
                leftPadding: 20
                color: "dark green"
                text: DateScript.createString(eventstart, eventend)
                font.pointSize: text_summary.font.pointSize/2
            }
            Text {
                id: text_location
                text: location
                color: "dark grey"
                leftPadding: 20
                font.pointSize: text_summary.font.pointSize/2.5
                maximumLineCount: 1
                elide: Text.ElideRight
                anchors.top: text_timestring.bottom
                anchors.left: text_timestring.left
                width: listView.width
            }
        }
    }
}