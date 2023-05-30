"""
ソケットclient
"""
from socket import *
from threading import *
from PyQt6.QtCore import Qt, pyqtSignal, QObject

# signalクラスを生成
class Signal(QObject):
    recv_signal = pyqtSignal(str)
    disconnect_signal = pyqtSignal()

# クライアントSocketクラス生成
class ClientSocket:
    # initializer
    def __init__(self, parent):
        self.parent = parent
        self.recv = Signal()
        self.recv.recv_signal.connect(self.parent.updateMessage)
        self.disconnet = Signal()
        self.disconnet.disconnect_signal.connect(self.parent.updateDisconnect)
        self.connectState = False
    
    # deinitializer
    def __del__(self):
        self.stop()

    def connectServer(self, ip, port):
        self.client = socket(AF_INET, SOCK_STREAM)

        try:
            self.client.connect((ip, port))
        except Exception as e:
            print('Connection Error: ', e)
            return False
        else:
            self.connectState = True
            self.thread = Thread(target=self.receive, args=(self.client,))
        return True
    
    def stop(self):
        self.connectState = False
        if hasattr(self, 'client'):
            self.client.close()
            del(self.client)
            print('Client側との通信を終了')
        
        return True
    
    def receive(self, client):
        # 通信が繋がっているとき
        while self.connectState:
            try:
                recv = client.recv(1024)
            except Exception as e:
                print('受信 Error: ', e)
                break
            else:
                # メッセージを文字列型にEncodingする作業
                message = str(recv, encoding='utf-8')
                if message:
                    self.recv.recv_signal.emit(message)
                    print('[受信]: ', message)
        
        self.stop()

    def send(self, message):
        if not self.connectState:
            return
        try:
            self.client.send(message.encode())
        except Exception as e:
            print('送信 Error: ', e)

# while True:
#     # 送信
#     msg = input("送りたいメッセージを入力：")
#     if msg == 'exit':
#         break
#     socket_client.send(msg.encode("UTF-8"))
#     # 返信
#     # 1024はバッファーのサイズ
#     recv_data = socket_client.recv(1024)
#     print(f"サーバーから受信したメッセージは：{recv_data.decode('UTF-8')}")
# # リンクを閉じる
# socket_client.close()
