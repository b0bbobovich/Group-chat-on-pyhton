from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConnectWindow(object):

    def setupUi(self, Form):
        Form.resize(600, 500)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")

        self.HostLabel = QtWidgets.QLabel(self.centralwidget)
        self.HostLabel.setGeometry(QtCore.QRect(100, 100, 90, 30))

        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)

        self.HostLabel.setFont(font)
        self.HostLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.HostLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HostLabel.setObjectName("HostLabel")

        self.PortLabel = QtWidgets.QLabel(self.centralwidget)
        self.PortLabel.setGeometry(QtCore.QRect(100, 200, 90, 30))

        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)

        self.PortLabel.setFont(font)
        self.PortLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.PortLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PortLabel.setObjectName("PortLabel")

        self.NameLabel = QtWidgets.QLabel(self.centralwidget)
        self.NameLabel.setGeometry(QtCore.QRect(100, 300, 90, 30))

        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)

        self.NameLabel.setFont(font)
        self.NameLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.NameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.NameLabel.setObjectName("NameLabel")

        self.HostTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.HostTextEdit.setGeometry(QtCore.QRect(250, 95, 250, 40))
        self.HostTextEdit.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.HostTextEdit.setObjectName("HostTextEdit")

        self.PortTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.PortTextEdit.setGeometry(QtCore.QRect(250, 195, 250, 40))
        self.PortTextEdit.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.PortTextEdit.setObjectName("PortTextEdit")

        self.NameTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.NameTextEdit.setGeometry(QtCore.QRect(250, 295, 250, 40))
        self.NameTextEdit.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.NameTextEdit.setObjectName("NameTextEdit")

        self.ConnectPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectPushButton.setGeometry(QtCore.QRect(225, 400, 150, 50))

        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(19)

        self.ConnectPushButton.setFont(font)
        self.ConnectPushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ConnectPushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 23, 23);")
        self.ConnectPushButton.setObjectName("ConnectPushButton")

        Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("ConnectWindow", "Chatik"))
        self.HostLabel.setText(_translate("ConnectWindow", "Server host"))
        self.PortLabel.setText(_translate("ConnectWindow", "Server port"))
        self.NameLabel.setText(_translate("ConnectWindow", "Your name"))
        self.ConnectPushButton.setText(_translate("ConnectWindow", "Connect"))
