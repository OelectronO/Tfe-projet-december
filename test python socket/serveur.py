
#----- A simple TCP based server program in Python using send() function -----

 

import socket

 

# Create a stream based socket(i.e, a TCP socket)

# operating on IPv4 addressing scheme

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 

# Bind and listen

serverSocket.bind(("localhost",5456))

serverSocket.listen()

 

# Accept connections

while(True):
    #vérification de connexion --> threading timer check à touts les connectés 


    (clientConnected, clientAddress) = serverSocket.accept()

    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))



    dataFromClient = clientConnected.recv(1024)

    print(dataFromClient.decode())



    # Send some data back to the client


    (clientConnected, clientAddress) = serverSocket.accept()
    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))
    dataFromClient = clientConnected.recv(1024)
    print(dataFromClient.decode())



    if dataFromClient.decode() == "OelectronO connexion vérif" :
        clientConnected.send("bonjour".encode())
    else :
        print("fail connect")
        clientConnected.send("erreur".encode())
