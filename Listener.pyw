import socket, win10toast, win32gui, win32con, ctypes, os, threading

s = socket.socket()
noti = win10toast.ToastNotifier()

s.bind(('', 6000))
s.listen(1)
s, addr = s.accept()
print('connected')

def display():
    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)


while True:
    try:
        recv = s.recv(1024).decode()
        t1 = threading.Thread(target=display)
        t1.start()
        if recv == '1':
            s.send('1'.encode())
        elif recv == '2':
            ctypes.windll.user32.LockWorkStation()
            s.send('2'.encode())
        elif recv == '3':
            os.system('shutdown /r /t 0')
            s.send('3'.encode())
        elif recv == '4':
            os.system('shutdown /p')
            s.send('4'.encode())
        else:
            recv = recv
            s.send('5'.encode())
            recv1 = s.recv(1024).decode()
            s.send('5'.encode())
            noti.show_toast(title=recv, msg=recv1)
    except:
        pass
