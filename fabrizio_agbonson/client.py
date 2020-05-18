import socket

adr_server = ("localhost",10000)

def Controllo() -> str:
    cond = True
    while cond:
        s = input("> ")
        if s == "w" or s == "s" or s == "a" or s == "d":
            cond = False
            return s
        elif s == "esc":
            return s
        else:
            print("valore sbagliato")



with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    while True:
        
        stringa = Controllo()
        s.sendto(stringa.encode("ascii"), (adr_server))
        


