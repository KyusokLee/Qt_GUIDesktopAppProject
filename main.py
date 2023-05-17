import sys
from PyQt6.QtCore import Qt, QSize, QUrl, QTranslator, QLocale
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidgetAction, QMainWindow
from PyQt6.QtGui import QIcon, QGuiApplication, QAction
from PyQt6.QtQml import QQmlApplicationEngine
class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.translator = QTranslator()
        self.translator.load("qtbase_ja.qm")
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

        translate_button = QPushButton('翻訳: ', self)
        translate_button.setFixedSize(150, 35)
        translate_button.clicked.connect(self.translateButtonClicked)
        layout.addWidget(translate_button, alignment= Qt.AlignmentFlag.AlignHCenter)

        self.chatResultLabel = QLabel('Chat: ', self)
        layout.addWidget(self.chatResultLabel)

        self.translateResultLabel = QLabel('翻訳結果:', self)
        layout.addWidget(self.translateResultLabel)

        self.setLayout(layout)
        self.show()

    def messageSendButtonClicked(self):
        print('send!')
        self.printTextEdit()
    
    def translateButtonClicked(self):
        print('translate!')
        self.inputText = self.text_edit.toPlainText()
        translatedText = self.translateToJapanese(self.inputText)
        self.translateResultLabel.setText('翻訳結果: ' + translatedText)

    def printTextEdit(self):
        self.sentText = self.text_edit.toPlainText()
        print(self.sentText)
        self.chatResultLabel.setText('Chat: ' + self.sentText)
    
    def translateToJapanese(self, text):
       print(text)
       resultText = self.translator.translate("", text)
       return resultText

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat = ChatWindow()
    sys.exit(app.exec())

