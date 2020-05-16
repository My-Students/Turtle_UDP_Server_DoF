import socket

#dati del servere a cui collegarsi
ip_server="127.0.0.1"
porta_server=2512

#creazione del socket
socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def main():
    print("-----------------------------------\nCOMANDI\nw: avanti \ns: indietro \na: gira a sinistra \nd: gira a destra \ne: incrementa movimento \nq: decrementa movimento \ni: annulla azione\nclose(): chiude il client \nt: chiude il server\n-----------------------------------\n")
    while True:
        azione=input("\ncomando: ")
        if azione=="close()":
            socket.close()
        socket.sendto(azione.encode(),(ip_server,porta_server))

if __name__ == "__main__":
    main()