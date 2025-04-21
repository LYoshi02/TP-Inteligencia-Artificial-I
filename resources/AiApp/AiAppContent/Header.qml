import QtQuick 6.5
import QtQuick.Controls 6.5

Item {
    width: 550
    height: 50

    Rectangle {
        anchors.fill: parent
        radius: 25
        color: "white"
        border.color: "#787D81"
           border.width: 2
        Text {
            anchors.centerIn: parent
            text: "Comparación de heurísticas por Algoritmo A*"
            font.pixelSize: 24
            font.bold: true
            color: "#222"
        }
    }
}
