from tkinter import *
from tkinter.messagebox import showinfo

ordersTab = [
    "Attack",
    "Retreat",
    "Hold your position",
    "Send different messages"
]


class CommanderGUI:
    commanderOrder = ""

    def __init__(self):
        self.window = Tk()
        self.orderRadio = IntVar()
        self._init_widgets()

    def run(self):
        self.window.mainloop()
        return self.commanderOrder

    def quit(self):
        self.window.destroy()

    def _init_widgets(self):
        self.window.resizable(0, 0)
        self.window.geometry("400x180")
        self.window.title("Byzantine Generals - Commander Interface")
        Label(self.window, text="Select the order as commander-in-chief of this expedition").pack()

        Radiobutton(self.window, text=ordersTab[0], variable=self.orderRadio, value=1).pack(anchor=W)
        Radiobutton(self.window, text=ordersTab[1], variable=self.orderRadio, value=2).pack(anchor=W)
        Radiobutton(self.window, text=ordersTab[2], variable=self.orderRadio, value=3).pack(anchor=W)
        Radiobutton(self.window, text=ordersTab[3], variable=self.orderRadio, value=4).pack(anchor=W)
        Button(self.window, text="Send the order to your Generals", command=self.sendCommanderOrder).pack()

    def sendCommanderOrder(self):
        choix = self.orderRadio.get()
        if choix == 0:
            showinfo("Alert", "You have to select an order !!!")
        elif choix == 1:
            showinfo("Alert", "You sent the order to Attack")
        elif choix == 2:
            showinfo("Alert", "You sent the order to Retreat")
        elif choix == 3:
            showinfo("Alert", "You sent the order to continue the siege")
        elif choix == 4:
            showinfo("Alert", "You sent a different message to each General")

        if choix == 0:
            self.commanderOrder = "No order selected !"
        else:
            self.commanderOrder = ordersTab[choix - 1]
            self.quit()


class GeneralGUI:
    generalMessage = ""

    def __init__(self):
        self.window = Tk()
        self.orderRadio = IntVar()
        self.orderLabel = StringVar()
        self.GeneralLabel = StringVar()
        self.init_widgets()

    def run(self):
        self.window.mainloop()
        return self.generalMessage

    def quit(self):
        self.window.destroy()

    def init_widgets(self):
        self.window.resizable(0, 0)
        self.window.geometry("400x180")
        self.window.title("Byzantine Generals - Generals Interface")
        Label(self.window, text="Select the message you want to send to your colleagues").pack()
        Label(self.window, textvariable=self.orderLabel, fg="red").pack()
        Label(self.window, textvariable=self.GeneralLabel, fg="green").pack()

        Radiobutton(self.window, text=ordersTab[0], variable=self.orderRadio, value=1).pack(anchor=W)
        Radiobutton(self.window, text=ordersTab[1], variable=self.orderRadio, value=2).pack(anchor=W)
        Radiobutton(self.window, text=ordersTab[2], variable=self.orderRadio, value=3).pack(anchor=W)
        Button(self.window, text="Send the message to other Generals", command=self.sendMessageToGenerals).pack()

    def updateOrderLabel(self, cmdOrder, general):
        self.orderLabel.set("The commander-in-chief has sent the order to ' {} ' !".format(cmdOrder))
        self.GeneralLabel.set(general)

    def sendMessageToGenerals(self):
        choix = self.orderRadio.get()
        if choix == 0:
            showinfo("Alert", "You have to select an order !!!")
        elif choix == 1:
            showinfo("Alert", "You sent to other Generals that the Commander ordered you to Attack")
        elif choix == 2:
            showinfo("Alert", "You sent to other Generals that the Commander ordered you to Retreat")
        elif choix == 3:
            showinfo("Alert", "You sent to other Generals that the Commander ordered you to continue the siege")

        if choix == 0:
            self.generalMessage = "No message selected !"
        else:
            self.generalMessage = ordersTab[choix - 1]
            self.quit()
