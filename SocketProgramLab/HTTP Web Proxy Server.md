# Lab 5: HTTP Web Proxy Server
---

> In this lab, you will learn how web proxy servers work and one of their basic functionalities –
caching. 
Your task is to develop a small web proxy server which is able to cache web pages. It is a very simple 
proxy server which only understands simple GET-requests, but is able to handle all kinds of objects -
not just HTML pages, but also images. 
Generally, when the client makes a request, the request is sent to the web server. The web server then 
processes the request and sends back a response message to the requesting client. In order to improve 
the performance we create a proxy server between the client and the web server. Now, both the 
request message sent by the client and the response message delivered by the web server pass through 
the proxy server. In other words, the client requests the objects via the proxy server. The proxy server 
will forward the client’s request to the web server. The web server will then generate a response 
message and deliver it to the proxy server, which in turn sends it to the client.
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210512211600151.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjY2MjMxOA==,size_16,color_FFFFFF,t_70#pic_center)
---

## Python	Code	for	the	Proxy	Server

```python
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

```
---
## Running	the	Proxy	Server
We use the link [http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html](http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html) to test our agent

![](https://img-blog.csdnimg.cn/20210512212101639.png#pic_center)


Then run the proxy server program locally
![](https://img-blog.csdnimg.cn/20210512212316575.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjY2MjMxOA==,size_16,color_FFFFFF,t_70#pic_center)
Then set up the web proxy
![](https://img-blog.csdnimg.cn/20210512212533203.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjY2MjMxOA==,size_16,color_FFFFFF,t_70#pic_center)

use ctrl+f5 to Force page refresh

![](https://img-blog.csdnimg.cn/20210512212843891.png#pic_center)Will generate html files in the same directory
Open the file to see the corresponding content
![](https://img-blog.csdnimg.cn/20210512212949895.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjY2MjMxOA==,size_16,color_FFFFFF,t_70#pic_center)

