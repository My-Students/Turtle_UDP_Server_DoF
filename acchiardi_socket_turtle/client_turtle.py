import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while(True):
    data = input("Inserisci il numero del comando,la lunghezza del tratto. (Es. 2,40):\n\t1 - right\n\t2 - left\n\t3 - forward\n\t4 - backward\n\t5 - shutdown\n")
    s.sendto(data.encode(),('localhost',2000))
    if(data == "5"):
        print("Shutdown.")
        break

s.close()