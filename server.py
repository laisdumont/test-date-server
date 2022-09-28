import threading
import socket
from datetime import datetime


def atender_cliente(client):
    data = client.recv(2048).decode()
    match data:
        case "1":
            print('ok')
            date = str(datetime.today().strftime("%d/%m/%Y"))
            client.send(date.encode('utf-8'))
        case "2":
            date = str(datetime.now().strftime("%H:%M"))
            client.send(date.encode('utf-8'))
        case "3":
            date = str(datetime.now().strftime("%d/%m/%Y %H:%M"))
            client.send(date.encode('utf-8'))
        case "4":
            client.close()

def server(host='localhost', port=8082):
    print("Server on...")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_address = (host, port)
    
    sock.bind(server_address)
    sock.listen(5)
    
    while True: 
        client, address = sock.accept()
        
        t1 = threading.Thread(target=atender_cliente, args=(client,))
        t1.start()

server()