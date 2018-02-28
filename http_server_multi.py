#Authors:
#Steven Wang 17392652

from socket import *
import threading

class ThreadedServer(threading.Thread):
    def __init__(self, con):
        threading.Thread.__init__(self)
        self.connectionSocket = con

    def run(self):
        while True:
            try:
                message = connectionSocket.recv(64)
                # if not message: break
                filename = message.split()[1]
                f = open(filename[1:], 'rb')
                outputdata = f.read()

                #Send one HTTP header line into socket
                connectionSocket.send(b'\nHTTP/1.1 200 OK\n\n')

                #Send the content of the requested file to the client
                for i in range(0,len(outputdata)):
                    connectionSocket.send(outputdata[i:i+1])

                connectionSocket.send(b'\r\n\r\n')
                connectionSocket.close()

            except IOError:
                #Send response message for file not found
                connectionSocket.send(b'HTTP/1.1 404 Not Found\r\n\r\n')

                #Close client socket
                connectionSocket.close()

if __name__ == '__main__':
    serverSocket = socket(AF_INET, SOCK_STREAM)
    hostname = '127.0.0.1'
    serverPort = 13011
    serverSocket.bind((hostname, serverPort))
    serverSocket.listen(1)
    print ('the web server is up on port:',serverPort)
    while True:
        print ("Ready to serve...")
        connectionSocket, addr = serverSocket.accept()
        thread_server = ThreadedServer(connectionSocket)
        thread_server.start()

    serverSocket.close()
