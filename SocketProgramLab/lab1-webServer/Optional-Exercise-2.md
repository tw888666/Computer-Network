## Optional Exercise 2
---

> Instead of using a browser, write your own HTTP client to test your server. Your client will connect to the server using a TCP connection, send an HTTP request to the server, and display the server 
response as an output. You can assume that the HTTP request sent is a GET method.The client should take command line arguments specifying the server IP address or host name, the port at which the server is listening, and the path at which the requested object is stored at the server. The following is an input command format to run the client.
client.py server_host server_port filename
 

---


## 实现
利用sys包实现命令行输入
其他大致相同注意测试的时候可能会出现多次拒绝服务的情况，多测试几次即可。注意服务器的端口号

---


## 代码
webClient.py

```python
import sys
from socket import *
"""
Command line argument: import sys sys.argv
sys.argv is a list,no need for split
"""
server_host = sys.argv[1]
server_port = sys.argv[2]
filename = sys.argv[3]

host_port = "%s:%s" % (server_host, server_port)
try:
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_host, int(server_port)))
    first_header = "GET /%s HTTP/1.1" % filename
    print(first_header)
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-us",
        "Host": host_port,
    }
    http_header = "\r\n".join("%s:%s" % (item, header[item]) for item in header)
    http_header += '\r\n'
    first_header += '\r\n'
    print(http_header)
    # request message
    # request line
    client_socket.send(first_header.encode())
    # header line
    client_socket.send(http_header.encode())
    # blank line
    client_socket.send('\r\n'.encode())

except IOError:

    sys.exit(1)
final = ""
response_message = client_socket.recv(1024).decode()
while response_message:
    final += response_message
    response_message = client_socket.recv(1024).decode()

client_socket.close()
print("final:\n%s" % final)




```

---



## 运行
---
#### 服务器端
运行webServer.py


#### 客户端


在pycharm终端 输入webClient.py hostname port filename

也可直接在终端运行,效果如下
![](https://img-blog.csdnimg.cn/20210520200944493.png)

![](https://img-blog.csdnimg.cn/20210520201003679.png)


---

