#Authors:
#Steven Wang 17392652

#127.0.0.1:12000/lab1.html
#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
#Fill in start
hostname = '127.0.0.1'
serverPort = 12000
serverSocket.bind((hostname, serverPort))
serverSocket.listen(1)
print ('the web server is up on port:',serverPort)
#Fill in end

while True:
    # Establish the connection
    print ("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(64)
        filename = message.split()[1]
        f = open(filename[1:], 'rb')
        outputdata = f.read()

        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send(b'\nHTTP/1.1 200 OK\n\n')
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i:i+1])

        connectionSocket.send(b'\r\n\r\n')
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
            #Fill in Start
            connectionSocket.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
            #Fill in end

            #Close client socket
            #Fill in start
            connectionSocket.close()
            #Fill in end
serverSocket.close()
