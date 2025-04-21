import QtQuick 6.5
import QtQuick.Layouts 6.5
Item {
    width: 850
    height: 300

    property string heuristicaSeleccionada: "Ambos"

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
            spacing: 10

            Row {
                spacing: 8

                Image {
                    source: "images/icono3.png"
                    width: 28
                    height: 28
                }

                Text {
                    text: "Visualización del grafo"
                    font.pixelSize: 18
                    font.bold: true
                    color: "#222"
                }
            }

            Row {
                spacing: 20

                /*Loader {
                    Layout.fillWidth: true
                    visible: heuristicaSeleccionada !== "Ambos"
                    source: heuristicaSeleccionada === "Manhattan"
                            ? "ManhattanView.qml"
                            : (heuristicaSeleccionada === "Línea recta"
                               ? "LineaRectaView.qml"
                               : "")
                }

                Loader {
                    Layout.fillWidth: true
                    visible: heuristicaSeleccionada === "Ambos"
                    source: "ManhattanView.qml"
                }

                Loader {
                    Layout.fillWidth: true
                    visible: heuristicaSeleccionada === "Ambos"
                    source: "LineaRectaView.qml"
                }*/
            }
        }
    }
}
