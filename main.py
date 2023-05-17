import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon
class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)
        push_button = QPushButton('送信')
        layout.addWidget(push_button)
        layout.addWidget(QLabel('Chat:'))
        self.setLayout(layout)
        self.setWindowTitle('Desktop Chat App')
        self.setGeometry(800, 300, 400, 300)
        self.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat = ChatWindow()
    sys.exit(app.exec())

