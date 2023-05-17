import sys
from PyQt6.QtCore import Qt, QSize, QUrl
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidgetAction, QMainWindow
from PyQt6.QtGui import QIcon, QGuiApplication, QAction
from PyQt6.QtQml import QQmlApplicationEngine
class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        engine = QQmlApplicationEngine()
        engine.load(QUrl('ApplicationWindow.qml'))
        if not engine.rootObjects():
            sys.exit(-1)

        self.setGeometry(800, 300, 400, 300)
        layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)
        self.setWindowTitle('Desktop Chat App')
        self.setWindowIcon(QIcon('ChatAppIcon.png'))

        # exitAction = QWidgetAction()
        # exitAction.setShortcut('command + Q')
        # exitAction.setStatusTip('Exit Application')
        # exitAction.triggered.connect(quit)
        
        push_button = QPushButton('送信', self)
        push_button.setFixedSize(150, 35)
        push_button.clicked.connect(self.messageSendButtonClicked)
        layout.addWidget(push_button, alignment= Qt.AlignmentFlag.AlignCenter)

        self.chatResultLabel = QLabel('Chat:', self)
        layout.addWidget(self.chatResultLabel)

        self.setLayout(layout)
        self.show()

    def messageSendButtonClicked(self):
        print('send!')
        self.printTextEdit()
    
    def printTextEdit(self):
        sentText = self.text_edit.toPlainText()
        print(sentText)
        self.chatResultLabel.setText(sentText)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat = ChatWindow()
    sys.exit(app.exec())

