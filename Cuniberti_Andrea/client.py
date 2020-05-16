
import socket
import turtle
from ast import literal_eval

IpAddress = 'localhost'
port = 5004

t = turtle.Turtle()
lista = []
cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while(True):
    #ricezione del messaggio

    #invio del messaggio
    mossa = input("inserisci la mossa: 1(avanti), 2(indietro), 3(sinistra), 4(destra)")
    lung = input("di quanto si deve muovere la tua tartaruga?")
    lista.append(t)
    lista.append(mossa)
    lista.append(lung)
    msg = (f"{lista}")
    print(msg)
    cli.sendto(msg.encode(),(IpAddress,port))

    #si può interrompere il collegamento digitando '$stop'
    if str(msg) == "$stop":
        break
    
    #ricezione messaggio di conferma
    data = cli.recv(8036)
    t = literal_eval(data)
    

cli.close()