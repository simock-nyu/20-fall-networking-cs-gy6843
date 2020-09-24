# 1648

from socket import *

# is_debugging = False

# def log(message):
#     if is_debugging == True:
#         print(message)

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.settimeout(5)
    clientSocket.connect((mailserver, port))
    # Fill in end

    # with clientSocket:
    recv = clientSocket.recv(1024).decode()
    # log(recv)
    # if recv[:3] != '220':
    #     log('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # log(recv1)
    # if recv1[:3] != '250':
    #     log('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    cmd = 'MAIL FROM:<scott.simock@nyu.edu>\r\n'
    clientSocket.send(cmd.encode())
    recv1 = clientSocket.recv(1024).decode()
    # log(recv1)
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    cmd = 'RCPT TO:<scott.simock@nyu.edu>\r\n'
    clientSocket.send(cmd.encode())
    recv1 = clientSocket.recv(1024).decode()
    # log(recv1)
    # Fill in end

    # # Send DATA command and print server response.
    # # Fill in start
    # cmd = 'DATA\r\n'
    # clientSocket.send(cmd.encode())
    # recv1 = clientSocket.recv(1024).decode()
    # # log(recv1)
    # # Fill in end

    # # Send message data.
    # # Fill in start
    # clientSocket.send(msg.encode())
    # recv1 = clientSocket.recv(1024).decode()
    # # Fill in end

    # # Message ends with a single period.
    # # Fill in start
    # clientSocket.send(endmsg.encode())
    # recv1 = clientSocket.recv(1024).decode()
    # # Fill in end

    # # Send QUIT command and get server response.
    # # Fill in start
    # cmd = 'QUIT\r\n'
    # clientSocket.send(cmd.encode())
    # recv1 = clientSocket.recv(1024).decode()
    # # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')