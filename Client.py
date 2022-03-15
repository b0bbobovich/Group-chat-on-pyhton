from socket import socket, AF_INET, SOCK_STREAM
from PyQt5 import QtCore, QtWidgets
import sys
from UI import connect_ui, chat_ui


class Client:
    def __init__(self):
        self.buffersize = 1024
        self.client_socket = socket(AF_INET, SOCK_STREAM)

        self.main_window = QtWidgets.QMainWindow()

        self.connect_widget = QtWidgets.QWidget(self.main_window)
        self.chat_widget = QtWidgets.QWidget(self.main_window)

        self.chat_widget.setHidden(True)
        self.chat_menu_ui = chat_ui.Ui_ChatWindow()

        self.connect_menu_ui = connect_ui.Ui_ConnectWindow()
        self.connect_menu_ui.setupUi(self.main_window)
        self.connect_menu_ui.ConnectPushButton.clicked.connect(self.on_btn_connect)

        self.main_window.show()

    def on_btn_connect(self):
        serverhost = self.connect_menu_ui.HostTextEdit.toPlainText()
        port = self.connect_menu_ui.PortTextEdit.toPlainText()
        name = self.connect_menu_ui.NameTextEdit.toPlainText()

        if not serverhost:
            serverhost = 'localhost'
        if not port:
            port = 5065
        else:
            port = int(port)
        if not name:
            name = 'user'

        if self.connecting(serverhost, port, name):
            print('Successful connection')
            self.connect_widget.setHidden(True)
            self.chat_menu_ui.setupUi(self.main_window)
            self.chat_menu_ui.SendPushButton.clicked.connect(self.send)
            self.chat_widget.setVisible(True)

            self.recv_thread_msg = ReceiveMessageThread(self.client_socket)
            self.recv_thread_msg.signal.connect(self.show_message)
            self.recv_thread_msg.start()

    def connecting(self, serverhost, port, name):
        try:
            self.client_socket.connect((serverhost, port))
            self.client_socket.sendall(name.encode('utf-8'))
            return True

        except ConnectionResetError:
            print('Connection failed')
            self.client_socket.close()
            return False

    def send(self):
        check_sending = True
        message = self.chat_menu_ui.ChatTextEdit.toPlainText()
        if message == 'fluggegecheimen':
            self.client_socket.sendall(message.encode('utf-8'))
            self.chat_menu_ui.textBrowser.clear()
            check_sending = False
            self.client_socket.close()
        else:
            try:
                self.client_socket.sendall(message.encode('utf-8'))
            except Exception:
                print('Unable to send message')
                check_sending = False
        if check_sending:
            self.chat_menu_ui.textBrowser.append('Me: ' + message)
            self.chat_menu_ui.ChatTextEdit.clear()

    def show_message(self, message):
        self.chat_menu_ui.textBrowser.append(message)


class ReceiveMessageThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket

    def run(self):
        self.receive_message()
        while True:
            self.receive_message()

    def receive_message(self):
        message = self.client_socket.recv(user.buffersize).decode('utf-8')
        self.signal.emit(message)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    user = Client()
    sys.exit(app.exec_())
