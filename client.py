import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destination = ("localhost", 8082)
sock.connect(destination)


while True:
    print("Digite uma das opçôes: ")
    print("[1] Data\n[2] Hora\n[3] Data e Hora\n[4] Sair")
    inputClient = input(">> ")
    sock.send(inputClient.encode("utf-8"))
    print(str(sock.recv(2048).decode()))
    print('\n---------------------\n')