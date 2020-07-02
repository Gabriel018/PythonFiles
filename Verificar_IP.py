import socket

hostname = socket.gethostname()
Meu_Ip = socket.gethostbyname(hostname)
print("Seu ip e : " + Meu_Ip)