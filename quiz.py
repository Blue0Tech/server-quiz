import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = '127.0.0.1'
port = 7999
server.bind((address,port))
server.listen()
print('server online')
questions = [
    'What is the capital of Thailand? A - Pakkret, B - Udon Thani, C - Bangkok, D - Surat Thani',
    'What is the largest country by population? A - India, B - China, C - USA, D - Brazil',
    'By which process do plants generate energy? A - photosynthesis, B - transpiration, C - osmosis, D - respiration'
]
answers = ['C','A','D']
cap = len(questions)

def clientThread(client,addr):
    score = 0
    try:
        client.send('Welcome to the quiz.'.encode('utf-8'))
        for i in range(0,cap):
            try:
                chosenIndex = random.randint(0,len(questions)-1)
                chosenQuestion = questions[chosenIndex]
                client.send(('\n\r'+chosenQuestion+'\n\r').encode('utf-8'))
                answer = client.recv(1).decode('utf-8').upper()
                if(answer==answers[chosenIndex]):
                    score += 1
                    client.send(('\n\rCorrect! Your score is currently '+str(score)).encode('utf-8'))
                else:
                    client.send(('\n\rIncorrect! The answer was '+answers[chosenIndex]+' and your score is currently '+str(score)).encode('utf-8'))
                questions.pop(chosenIndex)
                answers.pop(chosenIndex)
            except:
                continue
        client.send('\n\rThank you for participating in the quiz! Hope you enjoyed!'.encode('utf-8'))
    except:
        pass

while(True):
    conn,addr = server.accept()
    print(addr[0],'connected')
    thread = Thread(target=clientThread,args=(conn,addr))
    thread.start()