import socket
import threading

from interface import *
from traitor import *

HOST = ''
PORT = 46000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn_client = {}


class sendOrderToGenerals(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        nom = self.getName()

        if commander_order != ordersTab[3]:
            sendOrder = "GUI#{}#{}".format(nom, commander_order)
            self.connexion.send(sendOrder.encode())
        else:
            if nom == "General 1":
                sendOrder = "GUI#{}#{}".format(nom, ordersTab[0])
                self.connexion.send(sendOrder.encode())
            elif nom == "General 2":
                sendOrder = "GUI#{}#{}".format(nom, ordersTab[1])
                self.connexion.send(sendOrder.encode())
            elif nom == "General 3":
                sendOrder = "GUI#{}#{}".format(nom, ordersTab[2])
                self.connexion.send(sendOrder.encode())

        general_message = self.connexion.recv(1024).decode("Utf8")
        if nom == "General 1":
            updateGeneral_2_Array(2, nom, general_message)
            updateGeneral_3_Array(2, nom, general_message)
        elif nom == "General 2":
            updateGeneral_1_Array(2, nom, general_message)
            updateGeneral_3_Array(4, nom, general_message)
        elif nom == "General 3":
            updateGeneral_1_Array(4, nom, general_message)
            updateGeneral_2_Array(4, nom, general_message)

        for clt in conn_client:
            msg = "{} has sent you the message to ' {} '".format(nom, general_message)
            if conn_client[clt] != self.connexion:
                conn_client[clt].send(msg.encode("Utf8"))

        # showArrays()
        revealTraitor()


def startServer():
    mySocket.bind((HOST, PORT))
    print("Server has started, waiting for connection ...\n")
    mySocket.listen(3)


def acceptConnections():
    while len(conn_client) < 3:
        cnx, adr = mySocket.accept()
        conn_client[len(conn_client)] = cnx
        print("Messenger : General {} is in position and waiting for your orders !\t[{}:{}]".format(len(conn_client), adr[0], adr[1]))


def sendOrderThread():
    for generals in conn_client:
        th = sendOrderToGenerals(conn_client[generals])
        th.daemon = False
        th.setName("General {}".format(generals+1))
        th.start()


def updateGeneralsArray(value):
    if value != ordersTab[3]:
        updateGeneral_1_Array(0, "Commander", value)
        updateGeneral_2_Array(0, "Commander", value)
        updateGeneral_3_Array(0, "Commander", value)
    else:
        updateGeneral_1_Array(0, "Commander", ordersTab[0])
        updateGeneral_2_Array(0, "Commander", ordersTab[1])
        updateGeneral_3_Array(0, "Commander", ordersTab[2])


try:
    startServer()
    acceptConnections()

    commander_gui = CommanderGUI()
    commander_order = commander_gui.run()
    updateGeneralsArray(commander_order)
    print("\nYou have sent the order to {}\n".format(commander_order))

    sendOrderThread()

except (RuntimeError, TypeError, NameError):
    print("Out of bound exceptions !")
    sys.exit()
