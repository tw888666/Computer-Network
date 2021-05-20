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

