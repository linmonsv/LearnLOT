import QtQuick 2.12
import QtQuick.Window 2.12

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("US-100")

    RowLayout {

        Text{
            text: "distance : "
        }
        Text{
            objectName: "distance"
            text: "0.00 cm"
        }

    }
}
