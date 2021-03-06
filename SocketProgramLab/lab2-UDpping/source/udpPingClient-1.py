"""
@Author  : TW!

@Time    : 2021/5/9 18:06
"""
import time
from socket import *

serverPort = 12000
serverName = '192.168.233.128'
counter = 0
sums = 0
received, loss = 0, 0
maximum, minimum = 0.0, 0.0
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
        maximum = max(rtt, maximum)
        minimum = min(rtt, minimum)
        sums += rtt
        received += 1
    except timeout:
        print('Sequence %d: Request time out' % counter)
        loss += 1
        clientSocket.close()
    else:
        print('Sequence %d: Reply from %s    RTT = %.3fs' % (counter, serverName, rtt))

        clientSocket.close()
print('%s 的 Ping 统计信息: ' % serverName)
print('\t数据包: 已发送 = 10，已接收 = %d，丢失 = %d (%d%% 丢失)，' % (received, loss, loss / 10 * 100))
print('往返行程的估计时间(以秒为单位):')
print('\t最短 = %.3fs, 最长 = %.3fs, 平均 = %.3fs' % (minimum, maximum, sums / received))

