import socket
import turtle

#indirizzo e porta di questo server
ip="127.0.0.1"
porta=2512

#creazione del socket e binding
socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket.bind((ip,porta))

#variabili necessarie per la creazione e il movimento delle tartarughe
porte_tartarughe = [] 
tartarughe = {}

#variabile che indica il movimento
movimento = {}

#crea la tartaruga ed esegue il primo movimento
def creazione_tartaruga(porta_client, azione):
    movimento[porta_client[1]]=10
    tartarughe[porta_client[1]]=turtle.Turtle()
    if azione in comandi:   #controlla se il comando esiste
                comandi[azione](porta_client[1])

#definizione movimenti
def avanti(porta):
    tartarughe[porta].forward(movimento[porta])
def indietro(porta):
    tartarughe[porta].backward(movimento[porta])
def sinistra(porta):
    tartarughe[porta].left(movimento[porta])
def destra(porta):
    tartarughe[porta].right(movimento[porta])
def incrementaMovimento(porta):
    movimento[porta]+=1 
def decrementaMovimento(porta):
    movimento[porta]-=1 
def TerminateProcess(porta):
    print ("Server Terminato")
    TerminateProcess
def annulla(porta):
    tartarughe[porta].undo()

#comandi
comandi = {
    "w": avanti,
    "a": sinistra,
    "s": indietro,
    "d": destra,
    "e": incrementaMovimento,
    "q": decrementaMovimento,
    "t": TerminateProcess,
    "i": annulla,
}

def main():
    print ("Server Attivo")
    while True:
        #leggo i valori passati dal client
        valore_input, porta_client = socket.recvfrom(4096)
        azione=valore_input.decode()[0]

        #se la tartaruga esiste già la sposto altrimenti ne creo una
        if porta_client[1] in porte_tartarughe:
            if azione in comandi:   #controlla se il comando esiste
                comandi[azione](porta_client[1])
        else:
            porte_tartarughe.append(porta_client[1])
            creazione_tartaruga(porta_client,azione)
            #dati per il server
            print(f"creazione tartaruga con porta: {porta_client[1]}")

        #dati per il server
        print(f"porta: {porta_client[1]} - comando: {azione} - movimento: {movimento[porta_client[1]]}")

if __name__ == "__main__":
    main()



