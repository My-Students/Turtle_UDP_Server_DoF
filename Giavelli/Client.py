import socket

server_ip="127.0.0.1"
server_port=10000

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg=input(" w:fooward \n s:back \n a:left \n d:right \n Message: >> ")
    if msg=="exit()":
        s.close()
    s.sendto(msg.encode(),(server_ip,server_port))