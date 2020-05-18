import socket
import turtle
import random

colors  = ["red","green","blue","orange","purple","pink","yellow"]
bind_adr = ("localhost",10000)
SPEED = 100


def forward(t:turtle):
        t.forward(SPEED)
        
        
def left(t:turtle):
        t.left(90)
    
def right(t:turtle):
        t.right(90)
        
def backward(t:turtle):
        t.backward(SPEED)
        
    
        
def Crea_turtle()-> turtle:
    Player = turtle.Turtle()
    color = random.choice(colors)
    Player.color(color)
    Player.shape("turtle")
    
    Player.penup()
    
    return Player
    

user_dict = {}
function_move = {"w":forward,"s":backward,"a":left,"d":right}


with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    s.bind(bind_adr)
    

    print("creo il server...")
    print("avvio del server..")
    print("server[on]")
    
    while True:
        data_mov , addr = s.recvfrom(4096)

        if addr[1] in user_dict.keys():
            function_move[data_mov.decode()](user_dict[addr[1]])
        else:
            play = Crea_turtle()
            user_dict[addr[1]] = play
            function_move[data_mov.decode()](user_dict[addr[1]])
    
