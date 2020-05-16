import socket
import turtle
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
design = turtle.Turtle()
s.bind(('localhost',2000))
turtle_list = {}
while(True):
    data,address = s.recvfrom(4096)
    data_string = data.decode()
    if(data_string == "5"):
        print("Shutdown.")
        break
    else:
        x = data_string.split(",") #x = vettore con 2 valori, es. ["2","40"]
        command(int(x[0]), int(x[1]), address)

s.close

def command(move, number, turtle_address):
    if turtle_address not in turtle_list:
            turtle_list[turtle_address] = turtle.Turtle()
    switcher = {
        1: right,
        2: left,
        3: forward,
        4: backward
    }
    switcher[move](turtle_list[turtle_address],number)

def forward(turtle_address,number):
    turtle_list[turtle_address].forward(number)

def backward(turtle_address,number):
    turtle_list[turtle_address].backward(number)

def right(turtle_address,number):
    turtle_list[turtle_address].right(number)

def left(turtle_address,number):
    turtle_list[turtle_address].left(number)