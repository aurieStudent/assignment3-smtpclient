from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
mailserver = ('127.0.0.1', 1025) #lord I didn't choose a mail server
msg = "\r\n My message"
endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start

clientSocket=socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))

    # Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')


    # Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


    # Send MAIL FROM command and handle server response.
    # Fill in start
mailFrom="MAIL FROM: <auriecat@gmail.com>\r\n"
clientSocket.send(mailFrom.encode())
recv2=clientSocket.recv(1024).decode()
if recv2[:3] != '250':
    print('250 reply not received from server.')

    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
rcptTo="RCPT TO: <ac10984@nyu.edu>\r\n"
clientSocket.send(rcptTo.encode())
recv3=clientSocket.recv(1024).decode() #test
print("RCPT TO: ")
print(recv3)
if recv3[:3] != '250':
     print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
dataCo = "DATA\r\n"
clientSocket.send(dataCo.encode())
recv4=clientSocket.recv(1024).decode()
print("DATA: ")
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')



    # Fill in end

    # Send message data.
    # Fill in start
    #clientSocket.send(rcptTo) #test
msg = input("Enter message data: \r\n")
clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response. #end msg has the period
    # Fill in start
clientSocket.send(endmsg.encode())
recv5=clientSocket.recv(1024).decode()
print("After sending message: ")
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
quitCo="QUIT\r\n"
clientSocket.send(quitCo.encode())
recv6 = clientSocket.recv(1024).decode()
print("QUIT: ")
print(recv6)
if recv6[:3] != '221':
    print('221 reply not received from server.')
clientSocket.close() #whoops lol forgot to close the socket



if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

