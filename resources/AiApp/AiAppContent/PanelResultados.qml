import QtQuick 6.5

Item {
    width: 850
    height: 150

    Rectangle {
        width: parent.width
        height: parent.height
        color: "#000000"
        opacity: 0.1
        radius: 10
        x: 4
        y: 4
    }

    Rectangle {
        width: parent.width
        height: parent.height
        radius: 10
        color: "white"
        border.color: "#ccc"

        Column {
            anchors.fill: parent
            anchors.margins: 10
            spacing: 6

            Row {
                spacing: 8

                Image {
                    source: "images/icono4.png"
                    width: 28
                    height: 28
                }

                Text {
                    text: "Resultados"
                    font.pixelSize: 16
                    font.bold: true
                    color: "#222"
                }
            }
        }
    }
}
