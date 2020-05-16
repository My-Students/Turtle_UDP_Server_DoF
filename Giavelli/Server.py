import socket
import turtle
MOVE=10

server_ip="127.0.0.1"
server_port=10000
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((server_ip,server_port))

port_table=[]
turtle_dict={}

def turtle_create(address):
    turtle_dict[address]=turtle.Turtle()
    #turtle_dict[address]=TURTLE_KING.clone()
    #turtle_dict[address].showturtle()

def forward(t):
     t.forward(MOVE)

def backward(t):
    t.backward(MOVE)

def left(t):
    t.left(MOVE)

def right(t):
    t.right(MOVE) 

function={"w":forward,"s":backward,"a":left,"d":right}

while True:
    command,address = s.recvfrom(4096)
    movement=command.decode()
    if address in port_table:
        print(address)
        function[movement](turtle_dict[address])
    else:
        port_table.append(address)
        turtle_create(address)
        print(address)





