import socket
import turtle

ip = '127.0.0.1'
host = 80
indirizzo = (ip,host)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(indirizzo)

    print("Avviato")

    #Variabili per la gestione
    serv = []
    tut = []
    cont = 0

    while True:
        index = -1

        msg, address = s.recvfrom(4096)
        print(f"Collegamento stabilito con {address}")

        for x in range(len(serv)):
            print("controllo")
            if(serv[x] == (address)):
               index = x
               break 
        

        if (index == -1):
            print("controllo222")
            serv.append(address)
            tut.append(turtle.Turtle())
            index = cont
            cont = cont+1


       # splitto l'input del client 
        
        msg = (msg.decode()).split("_")  
        msg[1] = float(msg[1])

      # eseguo sulla corretta turtle il comando inserito
      
        if msg[0] == "forward":
            print("Forward")
            tut[index].forward(msg[1])
        if(msg[0] == "backward"):
            print("backward")
            tut[index].backward(msg[1])
        if(msg[0] == "right"):
            print("right")
            tut[index].right(msg[1])
        if(msg[0] == "left"):
            print("left")
            tut[index].left(msg[1])  

    s.close()

if __name__ == "__main__":
    main()
