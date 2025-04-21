import QtQuick 6.5
import QtQuick.Controls 6.5
import QtQuick.Layouts 6.5

ApplicationWindow {
    visible: true
    width: 1200
    height: 700
    title: "Algoritmo A*"

    Rectangle {
        anchors.fill: parent
        color: "#E6E6E0"
    }

    Header {
        width: 600
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        anchors.topMargin: 20
    }

    RowLayout {
        anchors.fill: parent
        anchors.margins: 20
        anchors.topMargin: 100
        spacing: 20

        ColumnLayout {
            Layout.fillWidth: true
            Layout.preferredWidth: 0.85
            Layout.fillHeight: true
            spacing: 20

            // Primera fila: Cargar Datos + Seleccionar Heurística
            RowLayout {
                Layout.fillWidth: true
                spacing: 20
                height: 100

                CardCargaDatos {
                    Layout.fillWidth: true
                    Layout.preferredWidth: 0.7
                    height: 100
                }

                CardSeleccionHeuristica {
                    Layout.fillWidth: true
                    Layout.preferredWidth: 0.3
                    height: 100
                }
            }

            // Segunda fila: Visualización del Grafo
            RowLayout {
                Layout.fillWidth: true
                Layout.preferredHeight: 350
                spacing: 20

                PanelVisualizacion {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                }
            }

            // Tercera fila: Resultados
            PanelResultados {
                Layout.fillWidth: true
                height: 130
            }
        }

        // Panel lateral
        PanelLateral {
            Layout.preferredWidth: 70
            Layout.alignment: Qt.AlignVCenter
            Layout.fillHeight: false
        }
    }
}
