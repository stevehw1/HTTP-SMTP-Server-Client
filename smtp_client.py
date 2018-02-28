#Authors:
#Steven Wang 17392652

from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Connect to the local host (an EECS server, where this code should be executed)
mailserver = "localhost"
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
mailPort = 25
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailPort))
#Fill in end
recv = clientSocket.recv(1024).decode()
print (recv)
if recv[:3] != '220':
    print ('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print (recv1)
if recv1[:3] != '250':
    print ('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
#print ("MAIL FROM:")
mailFrom = "MAIL FROM:<DonaldTrump@Whitehouse.gov>\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print (recv2)
if recv2[:1] != '250':
	print ('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
#print ("RCPT TO:"")
mailRCPT = 'RCPT TO:<stevehw1@uci.edu>\r\n'
clientSocket.send(mailRCPT.encode())
recv3 = clientSocket.recv(1024).decode()
print (recv3)
if recv3[:3] != '250':
	print ('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
#print("DATA")
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print (recv4)
if recv4[:3] != '354':
	print ('354 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start
#msg = input("Enter Input Here: ")
#so you can send your own message
#print("SENDING MESSAGE")
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
#print("MESSAGE END")
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print ('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
#print ("QUIT")
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print (recv6)
if recv6[:3] != '221':
	print ('221 reply not received from server.')

#print ("Mail Sent")
# Fill in end

#Link to codes: http://www.serversmtp.com/en/smtp-error
