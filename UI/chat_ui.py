from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChatWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("ChatWindow")
        Form.resize(499, 750)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")

        self.ChatTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.ChatTextEdit.setGeometry(QtCore.QRect(9, 9, 480, 150))
        self.ChatTextEdit.setStyleSheet("\n"
"background-color: rgb(248, 248, 248);")
        self.ChatTextEdit.setObjectName("ChatTextEdit")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(9, 168, 480, 511))
        self.textBrowser.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.textBrowser.setObjectName("textBrowser")

        self.SendPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendPushButton.setGeometry(QtCore.QRect(120, 690, 250, 40))

        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)

        self.SendPushButton.setFont(font)
        self.SendPushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 23, 23);")
        self.SendPushButton.setObjectName("SendPushButton")

        Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("ChatWindow", "Chatik"))
        self.SendPushButton.setText(_translate("ChatWindow", "Send"))
