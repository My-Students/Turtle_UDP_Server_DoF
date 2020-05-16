import socket as sck
import turtle


def server():
    # get the hostname
    host = "192.168.178.33"
    port = 6000  # initiate port

    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)  # get instance

    s.bind((host, port))  # bind host address and port

    listaTurtle = {}

    print("Server Online")

    while True:

        data, address = s.recvfrom(4096)  # receive message
        if address not in listaTurtle:
            print(f"Nuovo log: {address}")
            listaTurtle[address] = turtle.Turtle()

        if address in listaTurtle:
            print(f"Log esistente: {address}")
            istruction(data, listaTurtle[address])

        if not data.decode() or data.decode() == "exit":
            # if data is not received or data is the word 'exit' to end the connection break
            print("Close the connection")
            break

        s.sendto("Prossimo".encode(), address)  # send data to the client

    s.close()  # close the connection


def istruction(istr, t):
    istr = istr.decode()
    command = istr.split("_")[0]
    number = int(istr.split("_")[1])
    switcher = {
        "forward": forward,
        "f": forward,
        "backward": backward,
        "b": backward,
        "right": right,
        "r": right,
        "left": left,
        "l":left
    }
    switcher[command](t, number)
        

def forward(t, number):
    t.fd(number)

def backward(t, number):
    t.bk(number)

def right(t, number):
    t.right(number)

def left(t, number):
    t.left(number)



if __name__ == '__main__':
    server()
