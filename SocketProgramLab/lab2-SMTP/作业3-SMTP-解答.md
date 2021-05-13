# 套接字编程 作业3：SMTP
---

> 这个编程作业的目的是创建一个向任何接收方发送电子邮件的简单邮件客户。你的客户将必须与邮件服务器（如谷歌的电子邮件服务器）创建一个TCP连接，使用SMTP协议与该邮件服务器进行交谈，经该邮件服务器向某接收方（如你的朋友）发送一个电子邮件报文，最后关闭与该邮件服务器的TCP连接。
> 
> 对本作业，配套Web站点为你的客户提供了框架代码。你的任务是完善该代码并通过向不同的用户账户发送电子邮件来测试你的客户。你也可以尝试通过不同的服务器（例如谷歌的邮件服务器和你所在大学的邮件服务器）进行发送。

## 官方文档:
---
## 实现思路
---
本文采用qq邮箱来完成。
SMTP协议即简单邮件传输协议，允许用户按照标准发送/接收邮件。
在本文中，SMTP邮件客户端程序的基本流程如下：

 - 与qq邮件服务器建立TCP连接，域名"smtp.qq.com"，SMTP默认端口号25。建立连接后服务器将返回状态码220，代表服务就绪（类似HTTP，SMTP也使用状态码通知客户端状态信息）。
 - 发送"HELO"命令，开始与服务器的交互，服务器将返回状态码250（请求动作正确完成）。
 - <font color=#FF0000>发送"AUTH LOGIN"命令，开始验证身份，服务器将返回状态码334（服务器等待用户输入验证信息）！！！此处框架没有
 - 发送经过base64编码的用户名（本例中是qq邮箱的账号），服务器将返回状态码334（服务器等待用户输入验证信息）。
 - 发送经过base64编码的密码（本例中是qq邮箱的授权码），服务器将返回状态码235（用户验证成功）。
 - 发送"MAIL FROM"命令，并包含发件人邮箱地址，服务器将返回状态码250（请求动作正确完成）。
 - 发送"RCPT TO"命令，并包含收件人邮箱地址，服务器将返回状态码250（请求动作正确完成）。
 - 发送"DATA"命令，表示即将发送邮件内容，服务器将返回状态码354（开始邮件输入，以"."结束）。
 - 发送邮件内容，服务器将返回状态码250（请求动作正确完成）。
 - 发送"QUIT"命令，断开与邮件服务器的连接。
  
## 提示
 - 有些邮箱默认关闭SMTP服务，比如本文使用的qq邮箱。需要在设置中打开SMTP服务。另外，qq邮箱在打开SMTP服务后，会设置一个授权码，在程序使用这个授权码作为密码登录，而不是平时使用的密码。
 - 代码中带有"****"的内容的是需要自行设置的内容，包含：发件人邮箱，收件人邮箱，登录邮箱的用户名和密码。
 
## 代码

```python
import base64
from socket import *

msg = "\r\n I love computer networks!  🛫i love you❤"
endmsg = "\r\n.\r\n"
fromAddress = '957818618@qq.com'
toAddress = '1564640583@gmail.com'
contentType = 'text/plain'
subject = 'Computer Networking!'
mailServer = 'smtp.qq.com'
mailPort = 25
user = base64.b64encode(b'957818618@qq.com').decode()+'\r\n'
password = base64.b64encode(b'xqneczwbolmkbedc').decode()+'\r\n'
# Create socket called clientSocket and establish a TCP connection with mail server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, mailPort))
recv = clientSocket.recv(1024).decode()

print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
helloCommand = 'HELO Alice\r\n'
clientSocket.send(helloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# login user
clientSocket.send('AUTH LOGIN\r\n'.encode())
rec = clientSocket.recv(1024).decode()
print(rec)
clientSocket.send(user.encode())
rec = clientSocket.recv(1024).decode()
print(rec)
clientSocket.send(password.encode())
rec = clientSocket.recv(1024).decode()
print(rec)

# Send MAIL FROM command and print server response.
clientSocket.sendall(('MAIL FROM: <' + fromAddress + '>\r\n').encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
# Send RCPT TO command and print server response.
clientSocket.sendall(('RCPT TO: <' + toAddress + '>\r\n').encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
# Send DATA command and print server response.
clientSocket.sendall('DATA\r\n'.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
#
fp = open('faker.jpg', 'rb')
image = fp.read().decode()
fp.close()
# Send message data.
message = 'from:' + fromAddress + '\r\n'
message += 'to:' + toAddress + '\r\n'
message += 'subject:' + subject + '\r\n'
message += 'Content-ID:' + image + '\r\n'
message += 'Content-Type:' + contentType + '\t\n'
message += msg
clientSocket.sendall(message.encode())
# Message ends with a single period.
clientSocket.sendall(endmsg.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
# Send QUIT command and get server response.
clientSocket.send('QUIT\r\n'.encode())
clientSocket.close()
```

---
实现效果在这里不加以多说，运行成功则能在发送方的已发送邮件里看到或者在接收方的收件箱中看到。本教程主要精力在于后面的两个optional exercise。

---
## Optional Exercises

[optional 1](SocketProgramLab/lab2-SMTP/Optional-Exercises-1.md)


[optional 2](SocketProgramLab/lab2-SMTP/Optional-Exercises-2.md)
