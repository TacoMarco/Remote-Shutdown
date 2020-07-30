import socket, threading
from PyQt5 import QtCore, QtGui, QtWidgets

PORTNUM = 7000


class Ui_MainWindow(object):
    def connected(self):
        while True:
            try:
                self.s.connect(('', PORTNUM))
                break
            except:
                pass

        self.display.setEnabled(True)  # Enabling buttons
        self.lock.setEnabled(True)
        self.restart.setEnabled(True)
        self.shutdown.setEnabled(True)
        self.isConnected = True

    def send(self, value):
        self.s.send(value.encode())
        recv = self.s.recv(1024).decode()

    def notification_check(self):
        self.m = self.message_input.text()
        self.t = self.title_input.text()

        if (self.m and self.t != '') and self.isConnected:
            self.notification.setEnabled(True)
        else:
            self.notification.setEnabled(False)

    def notification_send(self):
        self.s.send(self.t.encode())
        recv = self.s.recv(1024).decode()
        self.s.send(self.m.encode())
        recv = self.s.recv(1024).decode()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(383, 450)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.display = QtWidgets.QPushButton(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(30, 20, 151, 71))
        self.display.setObjectName("display")
        self.display.setEnabled(False)

        self.lock = QtWidgets.QPushButton(self.centralwidget)
        self.lock.setGeometry(QtCore.QRect(30, 100, 151, 71))
        self.lock.setObjectName("lock")
        self.lock.setEnabled(False)

        self.restart = QtWidgets.QPushButton(self.centralwidget)
        self.restart.setGeometry(QtCore.QRect(30, 180, 151, 71))
        self.restart.setObjectName("restart")
        self.restart.setEnabled(False)

        self.shutdown = QtWidgets.QPushButton(self.centralwidget)
        self.shutdown.setGeometry(QtCore.QRect(30, 260, 151, 71))
        self.shutdown.setObjectName("shutdown")
        self.shutdown.setEnabled(False)

        self.notification = QtWidgets.QPushButton(self.centralwidget)
        self.notification.setGeometry(QtCore.QRect(210, 350, 151, 71))
        self.notification.setObjectName("notification")
        self.notification.setEnabled(False)

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setEnabled(True)
        self.title.setGeometry(QtCore.QRect(50, 350, 41, 31))
        self.title.setAutoFillBackground(True)
        self.title.setObjectName("title")
        self.title_input = QtWidgets.QLineEdit(self.centralwidget)
        self.title_input.setGeometry(QtCore.QRect(80, 360, 113, 20))
        self.title_input.setText("") 
        self.title_input.setObjectName("title_input")
        self.message_input = QtWidgets.QLineEdit(self.centralwidget)
        self.message_input.setGeometry(QtCore.QRect(80, 390, 113, 20))
        self.message_input.setText("")
        self.message_input.setObjectName("message_input")
        self.message = QtWidgets.QLabel(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(30, 390, 61, 21))
        self.message.setObjectName("message")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
    
        self.display.clicked.connect(lambda: self.send('1'))
        self.lock.clicked.connect(lambda: self.send('2'))
        self.restart.clicked.connect(lambda: self.send('3'))
        self.shutdown.clicked.connect(lambda: self.send('4'))
        self.notification.clicked.connect(self.notification_send)

        self.title_input.textChanged.connect(self.notification_check)  # Checks if it can enable notification only when it changes
        self.message_input.textChanged.connect(self.notification_check)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.isConnected = False
        self.s = socket.socket()

        t1 = threading.Thread(target=self.connected)
        t1.start()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Speech Rehab"))
        self.display.setText(_translate("MainWindow", "Turn off display"))
        self.lock.setText(_translate("MainWindow", "Lock"))
        self.restart.setText(_translate("MainWindow", "Restart"))
        self.shutdown.setText(_translate("MainWindow", "Shutdown"))
        self.notification.setText(_translate("MainWindow", "Send Notificaiton"))
        self.title.setText(_translate("MainWindow", "Title:"))
        self.message.setText(_translate("MainWindow", "Message:"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

