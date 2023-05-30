import sys
import socket_client
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtQml import QQmlApplicationEngine

# port指定
port = 1024

class QGroupBoxCustom(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        font = QFont("Helvetia", 13)
        font.setBold(True)
        self.setFont(font)

class QLineEditCustom(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        font = QFont("Helvetia", 13)
        font.setBold(False)
        self.setFont(font)

class QListWidgetCustom(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        font = QFont("Helvetia", 13)
        font.setBold(False)
        self.setFont(font)

class QTextEditCustom(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        font = QFont("Helvetia", 13)
        font.setBold(False)
        self.setFont(font)

class QLabelCustom(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        font = QFont("Helvetia", 13)
        font.setBold(True)
        self.setFont(font)

class QPushButtonConnect(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        font = QFont("Helvetia", 13)
        font.setBold(True)
        self.setFont(font)

class QPushButtonSend(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        font = QFont("Helvetia", 13)
        font.setBold(True)
        self.setFont(font)

class QPushButtonClear(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        font = QFont("Helvetia", 13)
        font.setBold(True)
        self.setFont(font)

class ChatClientWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.client = socket_client.ClientSocket(self)
        self.setStyle()
        self.initUI()
    
    def __del__(self):
        self.client.stop()
    
    def setStyle(self):
        with open("customStyle.css", 'r') as f:
            self.setStyleSheet(f.read())
    
    def initUI(self):
        # engine = QQmlApplicationEngine()
        # engine.load(QUrl('ApplicationWindow.qml'))
        # if not engine.rootObjects():
        #     sys.exit(-1)

        # self.setGeometry(800, 300, 400, 300)
        # layout = QVBoxLayout()
        # self.text_edit = QTextEdit()
        # layout.addWidget(self.text_edit)
        self.setWindowTitle('Desktop Chat App - Client')
        self.setWindowIcon(QIcon('ChatAppIcon.png'))

        # クライアント設定
        server_settingBox = QHBoxLayout()
        client_groupBox = QGroupBoxCustom('サーバー設定')
        server_settingBox.addWidget(client_groupBox)

        # Horizontal boxを生成
        server_connectionBox = QHBoxLayout()
        ip_label = QLabelCustom('Server IP')
        self.ip = QLineEditCustom()
        # IPアドレスを受信するような形式を設定
        self.ip.setInputMask('000.000.000.000;_')
        server_connectionBox.addWidget(ip_label)
        server_connectionBox.addWidget(self.ip)

        port_label = QLabelCustom('Server Port')
        self.port = QLineEditCustom(str(port))
        server_connectionBox.addWidget(port_label)
        server_connectionBox.addWidget(self.port)

        self.connect_button = QPushButtonConnect('接続')
        self.connect_button.clicked.connect(self.connectButtonClicked)
        server_connectionBox.addWidget(self.connect_button)

        client_groupBox.setLayout(server_connectionBox)

        # チャットの内容部分
        chat_informationBox = QHBoxLayout()
        chat_groupBox = QGroupBoxCustom('メッセージ')
        chat_informationBox.addWidget(chat_groupBox)

        chat_verticalBox = QVBoxLayout()

        recv_msg_label = QLabelCustom('受信したメッセージ')
        chat_verticalBox.addWidget(recv_msg_label)

        self.receiveMessage = QListWidgetCustom()
        chat_verticalBox.addWidget(self.receiveMessage)

        send_msg_label = QLabelCustom('送信するメッセージ')
        chat_verticalBox.addWidget(send_msg_label)

        self.sendMessage = QTextEditCustom()
        self.sendMessage.setFixedHeight(50)
        chat_verticalBox.addWidget(self.sendMessage)

        chat_horizontalBox = QHBoxLayout()

        chat_verticalBox.addLayout(chat_horizontalBox)
        self.send_button = QPushButtonSend('送信')
        self.send_button.setAutoDefault(True)
        self.send_button.clicked.connect(self.messageSendButtonClicked)

        self.clear_button = QPushButtonClear('チャット内容を消す')
        self.clear_button.clicked.connect(self.messageClearButtonClicked)

        chat_horizontalBox.addWidget(self.send_button)
        chat_horizontalBox.addWidget(self.clear_button)
        chat_groupBox.setLayout(chat_verticalBox)

        # 全体UIの揃え
        window_verticalBox = QVBoxLayout()
        window_verticalBox.addLayout(server_settingBox)
        window_verticalBox.addLayout(chat_informationBox)
        self.setLayout(window_verticalBox)
        self.show()
    
    def connectButtonClicked(self):
        if self.client.connectState == False:
            ip = self.ip.text()
            port = self.port.text()
            if self.client.connectServer(ip, int(port)):
                self.connect_button.setText('接続終了')
            else:
                self.client.stop()
                self.sendMessage.clear()
                self.receiveMessage.clear()
                self.connect_button.setText('接続')
        else:
            self.client.stop()
            self.sendMessage.clear()
            self.receiveMessage.clear()
            self.connect_button.setText('接続')

    def updateMessage(self, msg):
        self.receiveMessage.addItem(QListWidgetItem(msg))

    def updateDisconnect(self):
        self.connect_button.setText('接続')
    
    def messageSendButtonClicked(self):
        # TextEditに書いてある文字を持ってくる
        sendmsg = self.sendMessage.toPlainText()
        self.client.send(sendmsg)
        self.sendMessage.clear()
    
    def messageClearButtonClicked(self):
        self.receiveMessage.clear()
    
    # QWidgetの再定義間数: windowを閉じるとき、自動でsocketクラスを閉じるように
    def closeEvent(self, e):
        self.client.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # translator = QTranslator()
    # translator.load("app_ja")
    # app.installTranslator(translator)
    chat = ChatClientWindow()
    sys.exit(app.exec())

