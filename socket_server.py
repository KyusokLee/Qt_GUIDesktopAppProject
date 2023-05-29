"""
ソケットserver
"""
import socket
# Socket对象を作る
socket_server = socket.socket()
# ipとportをバインド
socket_server.bind(("localhost", 8888))
# Portをlisten
socket_server.listen(1)
conn, address = socket_server.accept()
print(f"clientからメッセージを受信した，内容は：{address}")

while True:
    data: str = conn.recv(1024).decode("UTF-8")
    print(f"客户端发来的消息是：{data}")
    # 返信
    msg = input("请输入你要和客户端回复的消息：")
    if msg == 'exit':
        break
    conn.send(msg.encode("UTF-8"))
# リンクを閉じる
conn.close()
socket_server.close()
