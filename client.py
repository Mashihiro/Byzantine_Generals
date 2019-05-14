import socket
import threading

from interface import *

HOST = '192.168.1.2'
PORT = 46000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class ReceiveOrderThenSend(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        message = self.connexion.recv(1024).decode("Utf8")
        commander_order = message.split("#")

        if commander_order[0] == "GUI":
            print("Commander's Messenger : The Commander has sent his order, ' {} '\n".format(commander_order[2]))

            general_gui = GeneralGUI()
            general_gui.updateOrderLabel(commander_order[2], commander_order[1])
            general_message = general_gui.run()
            self.connexion.send(general_message.encode("Utf8"))


class TransmitMessageToGenerals(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn
        # self.daemon = False

    def run(self):
        while True:
            message = self.connexion.recv(1024).decode("Utf8")
            commander_order = message.split("#")

            if not message:
                break

            if commander_order[0] != "GUI":
                print("General's Messenger : {}\n".format(message))


try:
    mySocket.connect((HOST, PORT))
    print("Server : You have successfully connected to the server !\n")

    ReceiveOrderThenSend(mySocket).start()
    TransmitMessageToGenerals(mySocket).start()
except socket.error:
    print("Server : An expected error has occurred !")
    sys.exit()
