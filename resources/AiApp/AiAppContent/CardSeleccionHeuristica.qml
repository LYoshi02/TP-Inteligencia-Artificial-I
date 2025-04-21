import QtQuick 6.5
import QtQuick.Controls 6.5

Item {
    width: 260
    height: 160

    signal heuristicaSeleccionada(string nuevaHeuristica)

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
        radius: 12
        color: "white"
        border.color: "#ddd"

        Column {
            spacing: 35
            anchors.fill: parent
            anchors.margins: 15

            // Título + ícono
            Row {
                spacing: 8
                anchors.left: parent.left

                Image {
                    source: "images/icono2.png"
                    width: 28
                    height: 28
                }

                Text {
                    text: "Seleccionar la heurística"
                    font.bold: true
                    font.pixelSize: 17
                    color: "#333"
                }
            }

            Item {
                width: 220
                height: 45
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.top: parent.top
                anchors.topMargin: 30

                // Sombra
                Rectangle {
                    width: parent.width - 10
                    height: parent.height - 10
                    x: 2
                    y: 2
                    radius: 12
                    color: "#000"
                    opacity: 0.15
                    z: -1
                }

                ComboBox {
                    id: combo
                    model: ["Manhattan", "Línea recta", "Ambos"]
                    width: parent.width - 10
                    height: parent.height - 10
                    font.pixelSize: 14
                    editable: false

                    indicator: Image {
                        source: "images/flechaAbajoIcon.png"
                        width: 25
                        height: 20
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.right: parent.right
                        anchors.rightMargin: 10
                    }

                    contentItem: Text {
                        text: combo.displayText
                        font.pixelSize: 18
                        color: "#333"
                        anchors.verticalCenter: parent.verticalCenter
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        elide: Text.ElideRight
                    }

                    background: Rectangle {
                        radius: 12
                        color: "#F4F4F4"
                        border.color: "#D0D0D0"

                        MouseArea {
                            anchors.fill: parent
                            hoverEnabled: true
                            onEntered: parent.color = "#E4E4E0"
                            onExited: parent.color = "#F4F4F4"
                            onReleased: heuristicaSeleccionada(combo.currentText)
                        }
                    }
                }
            }
        }
    }
}
