from PyQt6.QtWidgets import (QWidget, QPushButton, QFrame, QColorDialog, QApplication, QLabel, QSplashScreen)
from PyQt6.QtGui import QColor, QPainter, QFont, QPixmap
from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QTime, QTimer
import sys
from random import randint
import time


class Dashboard(QWidget):

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

        self.timer.start(1000)  # every 1 second,

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
        self.currSpeed.setText(str(newSpeed))

    def getRange(self):

        newRange = randint(40, 49)
        self.currRange.setText(str(newRange))

    def getBatt(self):

        newBatt = randint(0, 99)
        self.currBatt.setText(str(newBatt))

        newMapName = "batteries/battery"
        if (newBatt <= 0):
            newMapName += "0.png"
        elif (newBatt >= 96):
            newMapName += "24.png"
        else:
            newMapName += str((int(newBatt / 100.0 * 12) + 1)*2) + ".png"

        newBattMap = QPixmap(newMapName)
        newBattMap = newBattMap.scaledToHeight(96)
        self.batteryImage.setPixmap(newBattMap)

    def getTemp(self):

        newTemp = randint(60, 69)
        self.currTemp.setText(str(newTemp))

    def getCurrent(self):

        newCurrent = randint(80, 89)
        self.currCurrent.setText(str(newCurrent))

    def getPower(self):

        newPower = randint(90, 99)
        self.currPower.setText(str(newPower))


def progress():
    time.sleep(1)


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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    splash = SplashScreen()
    splash.show()
    progress()

    dash = Dashboard()
    dash.show()

    splash.finish(dash)

    sys.exit(app.exec())
