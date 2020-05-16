
import socket
import turtle
import random

server_ip = '127.0.0.1'
server_port = 10000

main_turtle = turtle.Turtle()   #creating a main turtle and hiding it
main_turtle.hideturtle()

turtles= {}   

connection_table = []   
def avanti(x,t):
    t.forward(x)
def indietro(x,t):
    t.backward(x)
def sinistra(x,t):
    t.left(x)
def destra(x,t):
    t.right(x)

comandi = {
    "w": avanti,
    "a": sinistra,
    "s": indietro,
    "d": destra,
}
lista_comandi = [k for k,_ in comandi.items()]  
    


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   
server.bind((server_ip, server_port))

while True:
    data, address = server.recvfrom(4096)    #storing data send and address of client
    data = data.decode()[0:]

    print(address)
    print(connection_table)
    print(turtles)

    if address in connection_table: 
        if data == "shutdown":    
            turtles.pop(address)
            connection_table.pop(connection_table.index(address))
        elif data in lista_comandi:   #check if data received is in data table
            comandi[data](10,turtles[address])
    else:   
        connection_table.append(address)
        turtles[address] = main_turtle.clone()
        turtles[address].showturtle()

