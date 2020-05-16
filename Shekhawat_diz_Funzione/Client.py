import socket
import turtle

ip = '127.0.0.1'
host = 80
indirizzo = (ip,host)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#com = input("Inserire il nome della turtle : ")
#s.sendto(com.encode(),indirizzo)
 
while True:
    com = input(">")
    if(com == "Exit"):
        s.sendto(com.encode(),indirizzo)
        break
    s.sendto(com.encode(),indirizzo)

s.close()