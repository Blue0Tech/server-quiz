import socket
from threading import Thread

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = '127.0.0.1'
port = 7999
client.connect((address,port))

def receive():
    while(True):
        try:
            response = client.recv(2048).decode('utf-8')
            print(response)
        except:
            print('Failed to connect')
            client.close()
            break

def send():
    try:
        client.send(input().encode('utf-8'))
    except:
        pass
    while(True):
        try:
            client.send(input()[0].encode('utf-8'))
        except:
            print('Failed to connect')
            pass

receive_thread = Thread(target=receive)
send_thread = Thread(target=send)
receive_thread.start()
send_thread.start()