# 套接字编程 作业1：Web服务器
---

> 在这个编程作业中，你将用Python语言开发一个简单的Web服务器，它仅能处理一个请求。具体而言，你的Web服务器将：
> 1. 当一个客户（浏览器）联系时创建一个连接套接字；
> 2. 从这个连接套接字接收HTTP请求；
 >3. 3.解释该请求以确定所请求的特定文件；
 >4. 4.从服务器的文件系统获得请求的文件；
 >5. 5.创建一个由请求的文件组成的HTTP响应报文，报文前面有首部行；
 >6. 6.经TCP连接向请求浏览器发送响应。如果浏览器请求一个在该服务器种不存在的文件，服务器应当返回一个“404 Not Found”差错报文。
 >
 >在配套网站中，我们提供了用于该服务器的框架代码，我们提供了用于该服务器的框架代码。你的任务是完善该代码，运行服务器，通过在不同主机上运行的浏览器发送请求来测试该服务器。如果运行你服务器的主机上已经有一个Web服务器在运行，你应当为该服务器使用一个不同于80端口的其他端口。


---
## 代码

```python
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
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\n\n'.encode())
        connectionSocket.close()
serverSocket.close()

```
HelloWorld.html

```
<head>Hello world!</head>
```

## 运行

---
### 服务器端:
![image](https://user-images.githubusercontent.com/68290480/118628371-20d05600-b7ff-11eb-89d8-c55df080b374.png)

在同一目录下保存.py文件和.html文件，运行.py作为服务器
### 客户端：
在另一台主机上打开浏览器，并输入"http://XXX.XXX.XXX.XXX:8888/HelloWorld.html" （其中"XXX.XXX.XXX.XXX"是服务器IP地址），以获取服务器上的HelloWorld.html文件。
正常情况下可以看到如下图所示：
![image](https://user-images.githubusercontent.com/68290480/118628691-70168680-b7ff-11eb-8a20-510f31d460ee.png)


输入新的不存在地址则出现所下图所示：

![image](https://user-images.githubusercontent.com/68290480/118629163-e915de00-b7ff-11eb-9b3b-b5202175d442.png)
注意http error 404

---
### Optional Exercise

---

[Optional-Exercise-1](Optional-Exercise-1.md)


[Optional-Exercise-2](Optional-Exercise-2.md)



