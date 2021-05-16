## Optional Exercise 1
---

>Currently, the program calculates the round-trip time for each packet and prints it out individually. 
Modify this to correspond to the way the standard ping program works. You will need to report 
the minimum, maximum, and average RTTs at the end of all pings from the client. In addition, 
calculate the packet loss rate (in percentage)

 

---


## 实现
在cmd中 ping baidu得到效果图如下所示：

![](https://img-blog.csdnimg.cn/20210516152536874.png)
现根据此效果模拟UDPping

---


## 代码
UDPclient.py

```python
"""
@Author  : TW![在这里插入图片描述](https://img-blog.csdnimg.cn/20210516152359179.png)

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

```

---



## 运行
---
##### 服务器端：
运行UDPserver.py即可
#### 客户端：
运行UDPclient.py
效果如下：

![](https://img-blog.csdnimg.cn/20210516152409958.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjY2MjMxOA==,size_16,color_FFFFFF,t_70)


---

