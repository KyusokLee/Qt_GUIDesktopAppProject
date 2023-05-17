import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material

ApplicationWindow {
  visible: true
  width: 640
  height: 480
  title: "Example App"

  Material.theme: id_theme_switch.position < 1 ? Material.Light : Material.Dark
  Material.foreground: id_theme_switch.position < 1 ? Material.Teal : Material.Orange
  Material.background: id_theme_switch.position < 1 ? Material.White : Material.Black
  Material.primary: id_theme_switch.position < 1 ? Material.Teal : Material.Orange
  Material.accent: id_theme_switch.position < 1 ? Material.Teal : Material.Orange

  Switch {
    id: id_theme_switch
    anchors.right: parent.right
    anchors.top: parent.top
    anchors.margins: 10
    text: "Dark theme"
    checked: false
  }

  Text {
    id: id_id_text
    anchors.centerIn: parent
    text: "Test String"
    color: id_theme_switch.position < 1 ? Material.color(Material.Teal) : Material.color(Material.Orange)
    font.pointSize: 24
  }
}