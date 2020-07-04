import socket, win10toast, ctypes
from os import system
from threading import Thread
from win32gui import SendMessage
from win32con import HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER

s = socket.socket()
noti = win10toast.ToastNotifier()

s.bind(('', 7000))
s.listen(1)
s, addr = s.accept()

def display():
    SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)

while True:
    try:
        recv = s.recv(1024).decode()
        if recv == '1':
            s.send('1'.encode())
            Thread(target=display).start()
        elif recv == '2':
            ctypes.windll.user32.LockWorkStation()
            s.send('2'.encode())
        elif recv == '3':
            system('shutdown /r /t 111110')
            s.send('3'.encode())
        elif recv == '4':
            system('shutdown /p')
            s.send('4'.encode())
        else:
            s.send('5'.encode())
            recv1 = s.recv(1024).decode()
            s.send('5'.encode())
            noti.show_toast(title=recv, msg=recv1)
    except:
        pass
