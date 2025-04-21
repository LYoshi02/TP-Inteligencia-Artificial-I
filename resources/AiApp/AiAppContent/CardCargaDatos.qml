import QtQuick 6.5

Item {
    width: 600
    height: 120

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
        border.width: 1

        Column {
            spacing: 10
            anchors.fill: parent
            anchors.margins: 10

            Row {
                spacing: 8
                Image {
                    source: "images/icono1.png"
                    width: 28
                    height: 28
                }
                Text {
                    text: "Cargar los datos"
                    font.bold: true
                    font.pixelSize: 17
                    color: "#222"
                }
            }

            Row {
                id: row
                width: 564
                height: 60
            }
        }
    }
}
