from socket import *
serverName = 'localhost'
serverPort = 8008
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort)) # Connect to the server

sentence = ('HELO evan')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('Client sent: ', sentence)
print('From Server: ', modifiedSentence.decode())

sentence = ('REQTIME')
clientSocket.send(sentence.encode())
print('Client sent: ', sentence)
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())

sentence = ('REQDATE')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('Client sent: ', sentence)
print('From Server: ', modifiedSentence.decode())

sentence = ('ECHO W#: W0759453')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('Client sent: ', sentence)
print('From Server: ', modifiedSentence.decode())

sentence = ('REQIP')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('Client sent: ', sentence)
print('From Server: ', modifiedSentence.decode())

sentence = ('BYE')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('W0123456 Client sent: ', sentence)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()