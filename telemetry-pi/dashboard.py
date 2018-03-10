import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer, QTime
from random import randint

class Dashboard(QWidget):
    mph = 35
    range = 40
    battery = 100
    temp = 80
    motorCurr = 60
    power = 60

    def __init__(self):
        super().__init__()
        self.initUI()

        self.timer = QTimer()
        self.timer.timeout.connect(self.setSpeed)
        self.timer.timeout.connect(self.setRange)
        self.timer.timeout.connect(self.setBatt)
        self.timer.timeout.connect(self.setTemp)
        self.timer.timeout.connect(self.setMotor)
        self.timer.timeout.connect(self.setPower)

        self.timer.start(1000)


    def initUI(self):
        self.setWindowTitle('Absolute')
        self.setStyleSheet("background-color:grey;")
        self.setGeometry(200, 100, 900, 500)
        self.setWindowTitle("my example")

        speedTitle = QLabel("Current Speed", self)
        newfont = QtGui.QFont("Arial", 36)
        speedTitle.setFont(newfont)
        speedTitle.resize(250, 50)
        speedTitle.move(20, 10)

        self.currSpeed = QLabel("speed", self)
        self.currSpeed.resize(300, 100)
        self.currSpeed.move(35, 55)
        self.currSpeed.setStyleSheet("background-color:grey;") #HOW TO SET BACKGROUND COLOR
        newfont = QtGui.QFont("Arial", 48, QtGui.QFont.Bold)
        self.currSpeed.setFont(newfont)

        rangeTitle = QLabel("Estimated Range", self)
        newfont = QtGui.QFont("Arial", 28)
        rangeTitle.setFont(newfont)
        rangeTitle.resize(250, 50)
        rangeTitle.move(20, 330)

        self.currRange = QLabel("range", self)
        self.currRange.resize(250, 80)
        self.currRange.move(50, 370)
        self.currRange.setStyleSheet("background-color:grey;")  # HOW TO SET BACKGROUND COLOR
        newfont = QtGui.QFont("Arial", 32, QtGui.QFont.Bold)
        self.currRange.setFont(newfont)

        battTitle = QLabel("Battery Level", self)
        newfont = QtGui.QFont("Arial", 26)
        battTitle.setFont(newfont)
        battTitle.resize(175, 30)
        battTitle.move(350, 280)

        self.currBatt = QLabel("battery", self)
        self.currBatt.resize(170, 70)
        self.currBatt.move(350, 320)
        self.currBatt.setStyleSheet("background-color:grey;")  # HOW TO SET BACKGROUND COLOR
        newfont = QtGui.QFont("Arial", 64, QtGui.QFont.Bold)
        self.currBatt.setFont(newfont)

        ####PUT BATTERY IMAGE ABOVE BATTERY LEVEL
        self.battImg = QLabel("🔋", self)
        self.battImg.resize(100, 100)
        self.battImg.move(400, 80)
        self.battImg.setStyleSheet("background-color:grey;")  # HOW TO SET BACKGROUND COLOR
        newfont = QtGui.QFont("Arial", 100, QtGui.QFont.Bold)
        self.battImg.setFont(newfont)

        tempTitle = QLabel("Cabin Temperature", self)
        newfont = QtGui.QFont("Arial", 26)
        tempTitle.setFont(newfont)
        tempTitle.resize(250, 30)
        tempTitle.move(650, 50)

        self.currTemp = QLabel("temp", self)
        self.currTemp.resize(100, 42)
        self.currTemp.move(730, 100)
        self.currTemp.setStyleSheet("background-color:grey;")  # HOW TO SET BACKGROUND COLOR
        newfont = QtGui.QFont("Arial", 40, QtGui.QFont.Bold)
        self.currTemp.setFont(newfont)

        motorTitle = QLabel("Motor Current", self)
        newfont = QtGui.QFont("Arial", 26)
        motorTitle.setFont(newfont)
        motorTitle.resize(175, 30)
        motorTitle.move(710, 170)

        self.currMotor = QLabel("mc", self)
        self.currMotor.resize(120, 42)
        self.currMotor.move(730, 210)
        self.currMotor.setStyleSheet("background-color:grey;")  # HOW TO SET BACKGROUND COLOR
        newfont = QtGui.QFont("Arial", 40, QtGui.QFont.Bold)
        self.currMotor.setFont(newfont)

        powerTitle = QLabel("Power", self)
        newfont = QtGui.QFont("Arial", 26)
        powerTitle.setFont(newfont)
        powerTitle.resize(175, 30)
        powerTitle.move(730, 280)

        self.currPower = QLabel("power", self)
        self.currPower.resize(170, 70)
        self.currPower.move(730, 330)
        self.currPower.setStyleSheet("background-color:grey;")  # HOW TO SET BACKGROUND COLOR
        newfont = QtGui.QFont("Arial", 40, QtGui.QFont.Bold)
        self.currPower.setFont(newfont)
        self.show()

    def setSpeed(self):
        self.mph += randint(-1, 1) # change to actual data
        if self.mph < 0:
            self.mph = 1
        x = str(self.mph)
        x += " mph"
        self.currSpeed.setText(x)

    def setRange(self):
        self.range += randint(-1, 0) # change to actual data
        if self.range < 0:
            self.range = 0
        x = str(self.range)
        x += " mi"
        self.currRange.setText(x)

    def setBatt(self):
        self.battery += randint(-1, 0) # change to actual data
        if self.battery < 0:
            self.battery = 0
        x = str(self.battery)
        x += "%"
        self.currBatt.setText(x)

    def setTemp(self):
        self.temp += randint(-1, 1) # change to actual data
        if self.temp < 0:
            self.temp = 0
        x = str(self.temp)
        x += " f"
        self.currTemp.setText(x)

    def setMotor(self):
        self.motorCurr += randint(-1, 1) # change to actual data
        if self.motorCurr < 0:
            self.motorCurr = 0
        x = str(self.motorCurr)
        x += " A"
        self.currMotor.setText(x)

    def setPower(self):
        self.power += randint(-1, 0) # change to actual data
        if self.power < 0:
            self.power = 0
        x = str(self.power)
        x += " W"
        self.currPower.setText(x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dash = Dashboard()

    sys.exit(app.exec_())
