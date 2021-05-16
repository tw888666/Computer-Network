## 作业2-UDPping程序
---

>在这个编程作业中，你将用Python编写一个客户ping程序。该客户将发送一个简单的ping报文，接受一个从服务器返回的pong报文，并确定从该客户发送ping报文到接收到pong报文为止的时延。该时延称为往返时延（RTT）。由该客户和服务器提供的功能类似于在现代操作系统中可用的标准ping程序，然而，标准的ping使用互联网控制报文协议（ICMP）（我们将在第4章中学习ICMP）。此时我们将创建一个非标准（但简单）的基于UDP的ping程序。
你的ping程序经UDP向目标服务器发送10个ping报文，对于每个报文，当对应的pong报文返回时，你的客户要确定和打印RTT。因为UDP是一个不可靠协议，由客户发送的分组可能会丢失。为此，客户不能无限期地等待对ping报文的回答。客户等待服务器回答的时间至多为1秒；如果没有收到回答，客户假定该分组丢失并相应地打印一条报文。
在此作业中，我们给出服务器的完整代码（在配套网站中可以找到。你的任务是编写客户代码，该代码与服务器代码非常类似。建议你先仔细学习服务器的代码，然后编写你的客户代码，可以不受限制地从服务器代码中剪贴代码行。

 

---


## 实现方法
UDPPinger.py
```python
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


```
---
UDPPingerServer.py

```python
import random
from socket import *
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message from the client
    message = message.upper()
    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
    # Otherwise, the server responds
    serverSocket.sendto(message, address)

```
---
## 运行
##### 服务器
运行UDPserver.py即可
#### 客户端
运行UDPclient.py
效果如下：
![](https://img-blog.csdnimg.cn/20210516140602591.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjY2MjMxOA==,size_16,color_FFFFFF,t_70)

---
## 本教程主要讲解Optional Exercises:

---

### Optional Exercise 1:
### Optional Exercise 2:
