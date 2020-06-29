import socket

hostname = socket.gethostname()
Meu_ip = socket.gethostbyname(hostname)
print("Seu Ip e: " + Meu_ip)