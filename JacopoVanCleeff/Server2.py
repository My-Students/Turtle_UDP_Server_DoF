import socket as sck
import turtle as tr

server_ip = 'localhost'
server_port = 8500

def left(t,x):
    t.left(x)

def right(t,x):
    t.right(x)

def forward(t,x):
    t.forward(x)

def backward(t,x):
    t.backward(x)

def main():

    t = {}

    move = {
        "forward" : forward,
        "backward": backward,
        "right"   : right,
        "left"    : left
    }

    server = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)  
    server.bind((server_ip, server_port))  

    print(f"\nServer avviato con successo \n\nporta: {server_port} ip: {server_ip}\n")

    while(True):
        
        print("Pronto per ricevere dati ...\n")

        indice = 1

        data, address = server.recvfrom(4096)
  
        #controllo per uscire 

        if(data.decode()[1:] == "close"): 
            break
        else:

            # controllo che nel dizionario non ci sia già l'indirizzo ip salvato e in caso aggiungerlo

            for i in t:
                if ((str)(address[0]) + "_" + (str)(address[1])) in t:
                    indice = i
                    break
              
            if(indice == 1):
                indice = (str)(address[0]) + "_" + (str)(address[1])
                t[indice] = tr.Turtle()
                
            # splitto l'input del client 

            data = (data.decode()).split("_")  

            comando = data[0]                 
            quantita = (float)(data[1])

            # eseguo sulla corretta turtle il comando inserito

            move[comando](t[indice],quantita)

    server.close()

if __name__ == "__main__":
    main()