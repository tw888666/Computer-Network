from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
severPort = 8888
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', severPort))
serverSocket.listen(1)
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, address = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        print(message)

        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\n'.encode())
        connectionSocket.send('Connection: close\n'.encode())
        # LengthString = 'Content-Length: '+str(len(outputdata))+'\n'
        # connectionSocket.send(LengthString.encode())
        connectionSocket.send('Connect-Type: text/html\n'.encode())
        connectionSocket.send('\n'.encode())
