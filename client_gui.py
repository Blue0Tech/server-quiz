import socket
from threading import Thread
from tkinter import *

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = '127.0.0.1'
port = 7999
client.connect((address,port))

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()
        self.login = Toplevel()
        self.login.title('Login')
        self.login.configure(height=300,width=300)
        self.login.resizable(False,False)
        self.loginLabel = Label(self.login,text='Enter nickname',font=('Helvetica',14))
        self.loginLabel.place(x=80,y=50)
        self.loginEntry = Entry(self.login,text='',font=('Helvetica',12),width=20)
        self.loginEntry.place(x=60,y=120)
        self.loginButton = Button(self.login,text='Continue',font=('Helvetica',12),width=10,command=lambda:self.signIn(self.loginEntry.get()))
        self.loginButton.place(x=100,y=200)
        self.Window.mainloop()
    def signIn(self,name):
        self.login.destroy()
        self.name = name
        receive_thread = Thread(target=self.receive)
        send_thread = Thread(target=self.send)
        receive_thread.start()
        send_thread.start()
    def receive(self):
        while(True):
            try:
                response = client.recv(2048).decode('utf-8')
                # print(response)
            except:
                # print('Failed to connect')
                client.close()
                break
    def send(self):
        try:
            client.send(self.name.encode('utf-8'))
        except:
            pass
        while(True):
            try:
                # client.send(input()[0].encode('utf-8'))
                pass
            except:
                # print('Failed to connect')
                pass

gui = GUI()