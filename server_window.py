import sys
import socket_server
import socket
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

port = 1024

class ChatServerWindow(QWidget):
    def __init__(self):
        super().__init__()
 
        self.server = socket_server.ServerSocket(self)
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('Desktop Chat App - Server')
        self.setWindowIcon(QIcon('ChatAppIcon.png'))
         
        # サーバー設定
        ipbox = QHBoxLayout()
 
        gb = QGroupBox('サーバー設定')
        ipbox.addWidget(gb)
 
        box = QHBoxLayout()
 
        label = QLabel('Server IP')
        self.ip = QLineEdit(socket.gethostbyname(socket.gethostname()))
        box.addWidget(label)
        box.addWidget(self.ip)
 
        label = QLabel('Server Port')
        self.port = QLineEdit(str(port))
        box.addWidget(label)
        box.addWidget(self.port)
 
        self.btn = QPushButton('サーバー実行')
        self.btn.setCheckable(True)        
        self.btn.toggled.connect(self.toggleButton)
        box.addWidget(self.btn)      
 
        gb.setLayout(box)
 
        # 接続クライアントの情報
        infobox = QHBoxLayout()
        gb = QGroupBox('Client 情報')
        infobox.addWidget(gb)
 
        box = QHBoxLayout()        
 
        self.guest = QTableWidget()        
        self.guest.setColumnCount(2)      
        self.guest.setHorizontalHeaderItem(0, QTableWidgetItem('ip'))
        self.guest.setHorizontalHeaderItem(1, QTableWidgetItem('port'))                
 
        box.addWidget(self.guest)
        gb.setLayout(box)
 
        # チャット内容の部分  
        gb = QGroupBox('メッセージ')        
        infobox.addWidget(gb)
 
        box = QVBoxLayout()        
 
        label = QLabel('受信したメッセージ')
        box.addWidget(label)
 
        self.msg = QListWidget()
        box.addWidget(self.msg)
 
        label = QLabel('送信するメッセージ')
        box.addWidget(label)
 
        self.sendmsg = QLineEdit()
        box.addWidget(self.sendmsg)
 
        hbox = QHBoxLayout()
         
        self.sendbtn = QPushButton('送信')
        self.sendbtn.clicked.connect(self.sendMsg)
        hbox.addWidget(self.sendbtn)
 
        self.clearbtn = QPushButton('チャット内容を消す')
        self.clearbtn.clicked.connect(self.clearMsg)
        hbox.addWidget(self.clearbtn)
 
        box.addLayout(hbox)
 
        gb.setLayout(box)
 
        # windowの全体UIの揃え
        vbox = QVBoxLayout()
        vbox.addLayout(ipbox)       
        vbox.addLayout(infobox)
        self.setLayout(vbox)
         
        self.show()
 
    def toggleButton(self, state):
        if state:
            ip = self.ip.text()
            port = self.port.text()
            if self.server.start(ip, int(port)):
                self.btn.setText('サーバー終了')                
        else:
            self.server.stop()
            self.msg.clear()
            self.btn.setText('サーバー実行')
 
    def updateClient(self, addr, isConnect = False):        
        row = self.guest.rowCount()        
        if isConnect:        
            self.guest.setRowCount(row+1)
            self.guest.setItem(row, 0, QTableWidgetItem(addr[0]))
            self.guest.setItem(row, 1, QTableWidgetItem(str(addr[1])))
        else:            
            for r in range(row):
                ip = self.guest.item(r, 0).text() # ip
                port = self.guest.item(r, 1).text() # port
                if addr[0]==ip and str(addr[1])==port:
                    self.guest.removeRow(r)
                    break
 
    def updateMsg(self, msg):
        self.msg.addItem(QListWidgetItem(msg))
        self.msg.setCurrentRow(self.msg.count()-1)
 
    def sendMsg(self):
        if not self.server.listenState:
            self.sendmsg.clear()
            return
        sendmsg = self.sendmsg.text()
        self.updateMsg(sendmsg)
        print(sendmsg)
        self.server.send(sendmsg)
        self.sendmsg.clear()
 
    def clearMsg(self):
        self.msg.clear()
 
    def closeEvent(self, e):
        self.server.stop()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_server = ChatServerWindow()
    sys.exit(app.exec())