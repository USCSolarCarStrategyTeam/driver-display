from PyQt6.QtWidgets import (QWidget, QPushButton, QFrame, QColorDialog, QApplication, QLabel, QSplashScreen)
from PyQt6.QtGui import QColor, QPainter, QFont, QPixmap
from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QTime, QTimer
import sys
from random import randint
import time
import threading
import serial


import asyncio




class Dashboard(QWidget):
    speed = 0
    temp = 0
    battery = 0
    current = 0
    power = 0
    range = 0

    def __init__(self):
        super(Dashboard, self).__init__()

        self.initUI()

        self.timer = QTimer()
        self.timer.timeout.connect(self.getSpeed)
        self.timer.timeout.connect(self.getRange)
        self.timer.timeout.connect(self.getBatt)
        self.timer.timeout.connect(self.getTemp)
        self.timer.timeout.connect(self.getCurrent)
        self.timer.timeout.connect(self.getPower)

        self.timer.start(0)  # every 1 second,

    def initUI(self):

        # Labels
        lbl1 = QLabel("Speed", self)
        lbl1.move(20, 20)

        lbl2 = QLabel("Est. Range", self)
        lbl2.move(20, 260)

        lbl3 = QLabel("Battery Level", self)
        lbl3.move(280, 230)

        lbl4 = QLabel("Cabin Temp", self)
        lbl4.move(510, 20)

        lbl5 = QLabel("Motor Current", self)
        lbl5.move(490, 170)

        lbl6 = QLabel("Power", self)
        lbl6.move(605, 320)

        # Values
        # Note: extra spaces prevent cutoff upon update
        self.currSpeed = QLabel("0   ", self)
        self.currSpeed.move(20, 55)

        self.currRange = QLabel("0   ", self)
        self.currRange.move(20, 300)

        self.currBatt = QLabel("0   ", self)
        self.currBatt.move(250, 240)

        self.currTemp = QLabel("0   ", self)
        self.currTemp.move(575, 55)

        self.currCurrent = QLabel("0   ", self)
        self.currCurrent.move(575, 205)

        self.currPower = QLabel("0   ", self)
        self.currPower.move(575, 355)

        # Units
        speedUnit = QLabel("mph", self)
        speedUnit.move(185, 150)

        rangeUnit = QLabel("mi.", self)
        rangeUnit.move(185, 395)

        battUnit = QLabel("%", self)
        battUnit.move(485, 278)

        tempUnit = QLabel("°F", self)
        tempUnit.move(670, 95)

        currentUnit = QLabel("A", self)
        currentUnit.move(675, 245)

        powerUnit = QLabel("W", self)
        powerUnit.move(670, 395)

        # Configure fonts
        textFont = QFont("Arial", 20)
        lbl1.setFont(textFont)
        lbl2.setFont(textFont)
        lbl3.setFont(textFont)
        lbl4.setFont(textFont)
        lbl5.setFont(textFont)
        lbl6.setFont(textFont)

        valueFontS = QFont("Arial", 50)
        valueFontM = QFont("Arial", 90)
        valueFontL = QFont("Arial", 130)
        self.currSpeed.setFont(valueFontM)
        self.currRange.setFont(valueFontM)
        self.currBatt.setFont(valueFontL)
        self.currTemp.setFont(valueFontS)
        self.currCurrent.setFont(valueFontS)
        self.currPower.setFont(valueFontS)

        unitFont = QFont("Arial", 20)
        speedUnit.setFont(unitFont)
        rangeUnit.setFont(unitFont)
        battUnit.setFont(unitFont)
        tempUnit.setFont(unitFont)
        currentUnit.setFont(unitFont)
        powerUnit.setFont(unitFont)

        # Configure colors
        textSS = "QLabel { color: gold; }"
        lbl1.setStyleSheet(textSS)
        lbl2.setStyleSheet(textSS)
        lbl3.setStyleSheet(textSS)
        lbl4.setStyleSheet(textSS)
        lbl5.setStyleSheet(textSS)
        lbl6.setStyleSheet(textSS)

        valueSS = "QLabel { color: black; }"
        self.currSpeed.setStyleSheet(valueSS)
        self.currRange.setStyleSheet(valueSS)
        self.currBatt.setStyleSheet(valueSS)
        self.currTemp.setStyleSheet(valueSS)
        self.currCurrent.setStyleSheet(valueSS)
        self.currPower.setStyleSheet(valueSS)

        unitSS = "QLabel { color: black; }"
        speedUnit.setStyleSheet(valueSS)
        rangeUnit.setStyleSheet(valueSS)
        battUnit.setStyleSheet(valueSS)
        tempUnit.setStyleSheet(valueSS)
        currentUnit.setStyleSheet(valueSS)
        powerUnit.setStyleSheet(valueSS)

        # Battery image
        battMap = QPixmap("batteries/battery24.png")
        battMap = battMap.scaledToHeight(96)
        self.batteryImage = QLabel(self)
        self.batteryImage.setPixmap(battMap)
        self.batteryImage.move(260, 115)

        # Configure dash color
        col = QColor(189, 32, 49)  # cardinal
        # col = QColor(169,169,169)   #grey
        p = self.palette()
        p.setColor(self.backgroundRole(), col)
        self.setPalette(p)

        # Basics
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(300, 300, 720, 480)
        self.center()
        # self.setWindowTitle('Solar Car Dash')
        # for making the dashboard fullscreen on rpi display
        # self.showMaximized()

    def keyPressEvent(self, e):

        if e.key() == Qt.Key.Key_Escape:
            self.close()

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def getSpeed(self):

        newSpeed = randint(50, 59)
        self.currSpeed.setText(str(self.speed))

    def getRange(self):

        newRange = randint(40, 49)
        self.currRange.setText(str(self.range))

    def getBatt(self):

        newBatt = randint(0, 99)
        self.currBatt.setText(str(self.battery))

        newMapName = "batteries/battery"
        if (int(self.battery) <= 0):
            newMapName += "0.png"
        elif (int(self.battery) >= 96):
            newMapName += "24.png"
        else:
            newMapName += str((int( int(self.battery) / 100.0 * 12) + 1) * 2) + ".png"

        newBattMap = QPixmap(newMapName)
        newBattMap = newBattMap.scaledToHeight(96)
        self.batteryImage.setPixmap(newBattMap)

    def getTemp(self):

        self.currTemp.setText(str(self.temp))

    def getCurrent(self):

        newCurrent = randint(80, 89)
        self.currCurrent.setText(str(self.current))

    def getPower(self):

        newPower = randint(90, 99)
        self.currPower.setText(str(self.power))



    # def data_loop(self):
    #     # Set up event loop
    #     loop = asyncio.get_event_loop()
    #     serial_task = loop.create_task(self.read_loop())



class start:
    Dashboard = None

    def __init__(self, dashboard):
     self.Dashboard = dashboard
    def progress(self):
        readthethread = ReadingThread(self.Dashboard)
        readthethread.start()


class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        self.center()
        pixmap = QPixmap("images/blackgradient.jpg")
        logo_pixmap = QPixmap("images/solar car logo.png")
        logo = QLabel(self)
        logo.setPixmap(logo_pixmap)
        logo.move(245, 125)

        self.setPixmap(pixmap)

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())





class ReadingThread(threading.Thread):
    def __init__(self, dashboard):
        super(ReadingThread, self).__init__()
        Dashboard = dashboard
    def run(self):
        self.read_loop()

    def read_loop(self):
        print("hi")
        file = open('test_input.txt', 'r')
        line = file.readline()
        print("dfjdnbf")
        while line != '':
            print(line.strip())
            # line = file.readline()
            data = line.split()
            # print("kdfjlsdkfj: " + data[0] + " " + data[1])
            print("data[0]: " + data[0])
            print("data[1]: " + data[1])

            if data[0] == "0":
                self.action(0, data[1])
            # range
            elif data[0] == "1":

                self.action(1, data[1])
            elif data[0] == "2":
                self.action(2, data[1])
            elif data[0] == "3":
                self.action (3, data[1])
            elif data[0] == "4":
                self.action(4, data[1])
            elif data[0] == "5":
                self.action(5, data[1])

            time.sleep(.5)

            line = file.readline()

    def action(self, number, value):
        if(number == 0):
            Dashboard.speed = value
            print("speed " + value)
        elif(number == 1):
            Dashboard.range=value;
            print("range " + value)
        elif (number == 2):
            Dashboard.battery = value
            print("battery " + value)
        elif (number == 3):
            Dashboard.temp = value
            print("temp " + value)
        elif (number == 4):
            Dashboard.current = value
            print("current " + value)
        elif(number == 5):
            Dashboard.power = value
            print("power " + value)








if __name__ == '__main__':

    app = QApplication(sys.argv)
    print("hasdfasdfi")

    splash = SplashScreen()
    splash.show()
    print("hi")
    dash = Dashboard()
    dash.show()

    starting = start(dash)
    starting.progress()



    # splash.finish(dash)
    # dash.read_loop()

    sys.exit(app.exec())
