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
        self.layout()
        self.submit(name)
        receive_thread = Thread(target=self.receive)
        receive_thread.start()
    def receive(self):
        while(True):
            try:
                response = client.recv(2048).decode('utf-8')
                # print(response)
                self.quizTextArea.config(state=NORMAL)
                self.quizTextArea.insert(END,response+'\n')
                self.quizTextArea.config(state=DISABLED)
                self.quizTextArea.see(END)
            except:
                # print('Failed to connect')
                pass
    def layout(self):
        self.Window.deiconify()
        self.Window.title('QUIZ')
        self.Window.resizable(False,False)
        self.Window.configure(width=470,height=550,bg='#17202A')
        self.quizTitle = Label(self.Window,text='Welcome '+self.name,font=('Helvetica',16))
        self.quizTitle.place(relx=0.32,rely=0.05)
        self.quizLine = Label(self.Window,width=450,bg='#ABB2B9')
        self.quizLine.place(relwidth=1,rely=0.12,relheight=0.01)
        self.quizTextArea = Text(self.Window,width=20,height=2,bg='#17202A',fg='#EAECEE',font=('Helvetica',14),pady=5)
        self.quizTextArea.pack(padx=(10,50))
        self.quizTextArea.place(relheight=0.65,relwidth=1,rely=0.15)
        self.scrollBar = Scrollbar(self.quizTextArea)
        self.scrollBar.place(relheight=1,relx=0.975)
        self.scrollBar.config(command=self.quizTextArea.yview)
        self.quizTextArea.config(yscrollcommand=self.scrollBar.set)
        self.quizLine2 = Label(self.Window,width=450,bg='#ABB2B9')
        self.quizLine2.place(relwidth=1,rely=0.82,relheight=0.01)
        self.buttonA = Button(self.Window,text='A',font=('Helvetica',14),command=lambda:self.submit('A'))
        self.buttonA.place(relx=0.15,rely=0.87)
        self.buttonB = Button(self.Window,text='B',font=('Helvetica',14),command=lambda:self.submit('B'))
        self.buttonB.place(relx=0.35,rely=0.87)
        self.buttonC = Button(self.Window,text='C',font=('Helvetica',14),command=lambda:self.submit('C'))
        self.buttonC.place(relx=0.55,rely=0.87)
        self.buttonD = Button(self.Window,text='D',font=('Helvetica',14),command=lambda:self.submit('D'))
        self.buttonD.place(relx=0.75,rely=0.87)
    def submit(self,msg):
        try:
            client.send(msg.encode('utf-8'))
        except:
            pass
        self.quizTextArea.config(state=NORMAL)
        self.quizTextArea.insert(END,'>'+msg+'\n')
        self.quizTextArea.config(state=DISABLED)
        self.quizTextArea.see(END)
gui = GUI()