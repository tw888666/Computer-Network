"""
@Author  : TW
@Time    : 2021/5/13 14:36
"""

import base64
import ssl
from socket import *

msg = "\r\n I love computer networks! this is good code! i love you❤"
endmsg = "\r\n.\r\n"
fromAddress = '95****@qq.com'
toAddress = '****@qq.com'
contentType = 'text/plain'
subject = 'Computer Networking!'
mailServer = 'smtp.qq.com'
mailPort = 465
user = base64.b64encode(b'95***@qq.com').decode()+'\r\n'
password = base64.b64encode(b'****').decode()+'\r\n' # 此密码可以去qq邮箱申请
# Create socket called clientSocket and establish a TCP connection with mail server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, mailPort))
# create SSL socket
clientSocketSSL = ssl.wrap_socket(clientSocket)

recv = clientSocketSSL.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
helloCommand = 'HELO Alice\r\n'
clientSocketSSL.send(helloCommand.encode())
recv1 = clientSocketSSL.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# login user
clientSocketSSL.send('AUTH LOGIN\r\n'.encode())
rec = clientSocketSSL.recv(1024).decode()
print(rec)
clientSocketSSL.send(user.encode())
rec = clientSocketSSL.recv(1024).decode()
print(rec)
clientSocketSSL.send(password.encode())
rec = clientSocketSSL.recv(1024).decode()
print(rec)

# Send MAIL FROM command and print server response.
clientSocketSSL.sendall(('MAIL FROM: <' + fromAddress + '>\r\n').encode())
recv1 = clientSocketSSL.recv(1024).decode()
print(recv1)
# Send RCPT TO command and print server response.
clientSocketSSL.sendall(('RCPT TO: <' + toAddress + '>\r\n').encode())
recv1 = clientSocketSSL.recv(1024).decode()
print(recv1)
# Send DATA command and print server response.
clientSocketSSL.sendall('DATA\r\n'.encode())
recv1 = clientSocketSSL.recv(1024).decode()
print(recv1)
# Send message data.
message = 'from:' + fromAddress + '\r\n'
message += 'to:' + toAddress + '\r\n'
message += 'subject:' + subject + '\r\n'
message += 'Content-Type:' + contentType + '\t\n'
message += msg
clientSocketSSL.sendall(message.encode())
# Message ends with a single period.
clientSocketSSL.sendall(endmsg.encode())
recv1 = clientSocketSSL.recv(1024).decode()
print(recv1)
# Send QUIT command and get server response.
clientSocketSSL.send('QUIT\r\n'.encode())
clientSocketSSL.close()
