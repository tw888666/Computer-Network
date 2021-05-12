"""
@Author  : TW
@Time    : 2021/5/10 23:33
"""
from socket import *
tcpSerPort = 5566
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('', tcpSerPort))
tcpSerSock.listen(5)
while True:
    # Start receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024).decode()
    print(message)
    # Extract the filename from the given message
    filename = message.split()[1].partition("//")[2].replace('/', '_')
    fileExist = "false"
    try:
        # Check wether the file exist in the cache
        f = open(filename, "r")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        for i in range(0, len(outputdata)):
            tcpCliSock.send(outputdata[i].encode())
        print('Read from cache')
        # Error handling for file not found in cache
    except IOError:
        print('fileExist is: ', fileExist)
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            hostn = message.split()[1].partition('//')[2].partition('/')[0]
            try:
                # Connect to the socket to port 80
                c.connect((hostn, 80))
                print('Socket connected to port 80 of the host')
                c.send(message.encode())
                # Read the response into buffer
                buff = c.recv(1024)
                tcpCliSock.send(buff)

                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                tmpFile = open("./" + filename, "w")
                tmpFile.writelines(buff.decode().replace('\r\n', '\n'))
                tmpFile.close()
            except:
                print("Illegal request")
        else:
            # HTTP response message for file not found
            print('File Not Found...Stupid Andy')
        # Close the client and the server sockets
        tcpCliSock.close()

tcpSerSock.close()
