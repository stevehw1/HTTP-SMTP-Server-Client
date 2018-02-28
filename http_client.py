#Authors:
#Steven Wang 17392652

from socket import *
import sys

#print("FIRE IT UP BABY")

hostname = sys.argv[1]
#print(hostname)

serverPort = sys.argv[2]
#print(serverPort)

fileName = sys.argv[3]
#print(fileName)

#print("Creating clientSocket")
clientSocket = socket(AF_INET,SOCK_STREAM)

#print("Connecting clientSocket")
clientSocket.connect((hostname, int(serverPort)))
#print("clientSocket connected!")

try:
    #get_message = "GET /" + fileName + " HTTP/1.1\r\n\r\n"
    #clientSocket.send(get_message.encode())

    get_line = "GET /" + fileName + " HTTP/1.1\r\n"
    host_line = "Host: " + hostname + ":" + serverPort + "\r\n\r\n"
    #accept_line = "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"+ "\r\n"
    #accept_encoding = "Accept-Encoding: gzip, deflate"+ "\r\n"
    #accept_lang = "Accept-Language: en-US,en;q=0.8" + "\r\n\r\n"

    header = get_line + host_line #+ accept_line + accept_encoding + accept_lang
    #print (header)
    clientSocket.send(header.encode())

    recv = clientSocket.recv(10000).decode()
    while (len(recv)>0):
        print(recv)
        recv = clientSocket.recv(10000)

except IOError:
    print('Error: 404 Not Found')
    clientSocket.close()
