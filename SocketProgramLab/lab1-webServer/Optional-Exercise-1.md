## Optional Exercise 1
---

> Currently, the web server handles only one HTTP request at a time. Implement a multithreaded server that is capable of serving multiple requests simultaneously. Using threading, first create a main thread 
in which your modified server listens for clients at a fixed port. When it receives a TCP connection request from a client, it will set up the TCP connection through another port and services the client request in a separate thread. There will be a separate TCP connection in a separatethread for each request/response pair.

 

---


## 实现
使用threading包 重写run方法当线程start时会自动执行run方法

---


## 代码
MultiThreadServer.py

```python
import datetime
import threading
from socket import *
""" 
In each thread, do not put connectionSocket.close()in thread while loop.
"""


class ClientThread(threading.Thread):
    def __init__(self, connect, address):
        threading.Thread.__init__(self)
        self.connectionSocket = connect
        self.addr = address

    def run(self):
        while True:
            try:
                message = connectionSocket.recv(1024).decode()
                if not message:
                    break
                print("message:\n%s" % message)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()
                now = datetime.datetime.now()
                # Send one HTTP header line into socket

                first_header = "HTTP/1.1 200 OK\r\n"
                header_info = {
                    "Date": now.strftime("%Y-%m-%d %H:%M"),
                    "Content-Length": str(len(outputdata)),
                    "Keep-Alive": "timeout=%d,max=%d" % (10, 100),
                    "Connection": "Keep-Alive",
                    "Content-Type": "text/html"
                }

                following_header = "\r\n".join("%s:%s" % (item, header_info[item]) for item in header_info)
                following_header += "\r\n"
                connectionSocket.send(first_header.encode())
                connectionSocket.send(following_header.encode())
                connectionSocket.send('\r\n'.encode())

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

            except IOError:
                # Send response message for file not found
                connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
                # connectionSocket.send('404 Not Found\r\n'.encode())
                # Close client socket   


if __name__ == '__main__':
    serverSocket = socket(AF_INET, SOCK_STREAM)  # Prepare a sever socket
    serverPort = 8848
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        print('address: %s' % addr[0])
        client_thread = ClientThread(connectionSocket, addr)
        client_thread.setDaemon(True)
        client_thread.start()   # 执行run
    serverSocket.close()


```

---



## 运行
---

运行MultiThreadServer.py
并在浏览器上输入hostname:port/filename(自行填写)
效果如下：
![](https://img-blog.csdnimg.cn/20210520195629473.png)




---

