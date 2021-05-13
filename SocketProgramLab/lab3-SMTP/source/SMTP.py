import base64
from socket import *

msg = "\r\n I love computer networks!  🛫i love you❤"
endmsg = "\r\n.\r\n"
fromAddress = '***@qq.com'
toAddress = '****@gmail.com'
contentType = 'text/plain'
subject = 'Computer Networking!'
mailServer = 'smtp.qq.com'
mailPort = 25
user = base64.b64encode(b'9***@qq.com').decode()+'\r\n'
password = base64.b64encode(b'****').decode()+'\r\n' # 此处自行在qq邮箱界面申请
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
