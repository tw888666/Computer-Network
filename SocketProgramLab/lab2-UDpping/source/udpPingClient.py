"""
@Author  : TW
@Time    : 2021/5/9 18:06
"""
import time
from socket import *

serverPort = 12000
serverName = '192.168.233.128' # 自行填写
counter = 0
while counter < 10:
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = 'ping ' + str(counter)
    counter += 1
    try:
        clientSocket.settimeout(1)
        begin = time.time()
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifyMessage, severAddress = clientSocket.recvfrom(1024)
        end = time.time()
        rtt = end - begin
    except timeout:
        print('Sequence %d: Request time out' % counter)
        clientSocket.close()
    else:
        print('Sequence %d: Reply from %s    RTT = %.3fs' % (counter, serverName, rtt))
        clientSocket.close()
