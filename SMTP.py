#import abilities
from socket import *


msg = "\r\n I love Computer Networks"  #body meesage
endmsg = "\r\n.\r\n" #character returns and line returns end message

#choosing a mail server smtp.gmail.com, 587
#mailserver = ("mail.smtp2go.com", 2525) #Fill in start #Fill in end
mailserver = ("smtp.gmail.com", 587) #Fill in start #Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM) #internet and socket protocols
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024) #client socket will recieve amount of data equals 1024
print("Message after connection request:", recv)
if recv[:3] != '220': #if the msg not recieved
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'Helo Alice\r\n' #server reply
clientSocket.send(heloCommand.encode()) #send the reply msg
recv1 = clientSocket.recv(1024) #receive the msg
print(recv1)
if recv1[:3] != '250': #if the msg not recieved
    print('250 reply not received from server.')


# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <anyemailid@gmail.com> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024) #amount of data recieved
print("After MAIL FROM command: ", recv2)
if recv1[:3] != '250': #if the data not recieved
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptTo = "RCPT TO: <destination@gmail.com> \r\n" #reciepent
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024) #amount of data recieved
print("After RCPT TO command: ",recv3)
if recv1[:3] != '250': #if the data not recieved
    print('250 reply not received from server.')

# Send DATA command and print server response.
data = "DATA\r\n"
clientSocket.send(data.encode()) #send the data
recv4 = clientSocket.recv(1024) #total size of the msg
print("After DATA command: ", recv4)
if recv1[:3] != '250': #if the msg not recieved
    print('250 reply not received from server.')

# Send message data.
subject = "Subject: SMTP mail client testing \r\n\r\n"
clientSocket.send(subject.encode())
message = input("Enter your message: ") #input the message
#fill in end #msg ends with a single period
clientSocket.send(message.encode())
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024) #amountof data to be send
print("Response after sending message body:", recv_msg.decode())
if recv1[:3] != '250': #if the msg doesn't print properly
    print('250 reply not received from server.')

# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode()) #tells the server the interaction should be terminated
message=clientSocket.recv(1024)
print (message)
clientSocket.close() #close the socket