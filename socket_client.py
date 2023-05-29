"""
ソケットclient
"""
import socket
# socket对象を作る
socket_client = socket.socket()
# サーバーにリンク
socket_client.connect(("localhost", 8888))

while True:
    # 送信
    msg = input("送りたいメッセージを入力：")
    if msg == 'exit':
        break
    socket_client.send(msg.encode("UTF-8"))
    # 返信
    # 1024はバッファーのサイズ
    recv_data = socket_client.recv(1024)
    print(f"サーバーから受信したメッセージは：{recv_data.decode('UTF-8')}")
# リンクを閉じる
socket_client.close()
