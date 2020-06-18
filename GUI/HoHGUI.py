import sys
import hypixel
import GildenGUI
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QLineEdit
from PyQt5.QtGui import QIcon, QFont

API_KEYS = ['f2c943c0-f3ed-449e-9de5-67a4b397434a']
hypixel.setKeys(API_KEYS)



class MainFenster(QWidget):
    def __init__(self):
        super().__init__()
        self.InitMe()

    def InitMe(self):
        QToolTip.setFont(QFont("Arial", 12))
        self.buttonG = QPushButton("Gilde", self)
        self.buttonG.resize(100,30)
        self.buttonG.move(50,390)
        self.buttonG.setToolTip("Wertet <b>alle</b> Spieler der Gilde aus")
        self.input1 = QLineEdit(self)
        self.input1.setMaxLength(16)
        self.input1.resize(100,30)
        self.input1.move(50,350)
        self.input1.setFont(QFont("Arial", 12))                
        self.buttonG.clicked.connect(self.ausgabe)
        self.setGeometry(600,300,800,450)
        self.setWindowTitle("House of Herbs")
        self.setWindowIcon(QIcon("HoH.png"))
        self.show()

    def ausgabe(self):
        name = self.input1.text()
        Player = hypixel.Player(name)
        PlayerInfo = Player.getPlayerInfo()
        PlayerGilde = Player.getGuildID()
        Gilde = hypixel.Guild(PlayerGilde)
        GildenMember = Gilde.getMembers()
        print(PlayerGilde)
        
app = QApplication(sys.argv)
w = MainFenster()

sys.exit(app.exec_())