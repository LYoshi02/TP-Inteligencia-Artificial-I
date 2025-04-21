import QtQuick 6.5
import QtQuick.Controls 6.5

Item {
    width: 70
    height: 400

    Rectangle {
        width: parent.width
        height: parent.height
        color: "#000000"
        opacity: 0.1
        radius: 35
        x: 4
        y: 4
    }

    Rectangle {
        width: parent.width
        height: parent.height
        color: "white"
        radius: 35

        Column {
            anchors.fill: parent
            anchors.margins: 10
            spacing: 20
            anchors.horizontalCenter: parent.horizontalCenter

            Button {
                width: 50
                height: 50
                focusPolicy: Qt.NoFocus
                background: Rectangle {
                    color: "black"
                    radius: 25
                }

                contentItem: Image {
                    source: "images/play.png"
                    width: 24
                    height: 24
                    anchors.centerIn: parent
                }

                onClicked: console.log("Play clicked!")
            }

            Rectangle {
                width: 50
                height: 1
                color: "#ddd"
                anchors.horizontalCenter: parent.horizontalCenter
            }

            Column {
                spacing: 20
                anchors.horizontalCenter: parent.horizontalCenter

                Repeater {
                    model: [
                        "images/flechaDerechaIcon.png",
                        "images/flechaIzqIcon.png",
                        "images/aleatorioIcon.png",
                        "images/tecladoIcon.png",
                        "images/basuraIcon.png"
                    ]

                    delegate: Button {
                        width: 40
                        height: 40
                        focusPolicy: Qt.NoFocus
                        background: Rectangle {
                            color: control.down ? "#E0E0E0" : (control.hovered ? "#F5F5F5" : "grey")
                            radius: 9
                            border.color: "grey"
                        }

                        contentItem: Image {
                            source: modelData
                            width: 24
                            height: 24
                            anchors.centerIn: parent
                        }

                        onClicked: console.log("Clicked on", modelData)
                    }
                }
            }
        }
    }
}
