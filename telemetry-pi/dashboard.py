from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
                             QColorDialog, QApplication, QLabel, QDesktopWidget)
from PyQt5.QtGui import QColor, QPainter, QFont, QPixmap
from PyQt5.QtCore import Qt, QTime, QTimer
import sys
from random import randint


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

        self.timer.start(1000)

    def initUI(self):

        # Labels
        lbl1 = QLabel("Current Speed", self)
        lbl1.move(25, 25)

        lbl2 = QLabel("Estimated Range", self)
        lbl2.move(25, 270)

        lbl3 = QLabel("Battery Level", self)
        lbl3.move(280, 230)

        lbl4 = QLabel("Cabin Temperature", self)
        lbl4.move(450, 25)

        lbl5 = QLabel("Motor Current", self)
        lbl5.move(515, 175)

        lbl6 = QLabel("Power", self)
        lbl6.move(600, 320)

        # Values
        # Note: extra spaces prevent cutoff upon update
        self.currSpeed = QLabel("0   ", self)
        self.currSpeed.move(25, 55)

        self.currRange = QLabel("0   ", self)
        self.currRange.move(25, 300)

        self.currBatt = QLabel("0   ", self)
        self.currBatt.move(250, 240)

        self.currTemp = QLabel("0   ", self)
        self.currTemp.move(580, 55)

        self.currCurrent = QLabel("0   ", self)
        self.currCurrent.move(580, 205)

        self.currPower = QLabel("0   ", self)
        self.currPower.move(580, 350)

        # Units
        speedUnit = QLabel("mph", self)
        speedUnit.move(175, 150)

        rangeUnit = QLabel("mi.", self)
        rangeUnit.move(175, 395)

        battUnit = QLabel("%", self)
        battUnit.move(465, 278)

        tempUnit = QLabel("°F", self)
        tempUnit.move(660, 92)

        currentUnit = QLabel("A", self)
        currentUnit.move(660, 242)

        powerUnit = QLabel("W", self)
        powerUnit.move(660, 387)

        # Configure fonts
        textFont = QFont("Arial", 20)
        lbl1.setFont(textFont)
        lbl2.setFont(textFont)
        lbl3.setFont(textFont)
        lbl4.setFont(textFont)
        lbl5.setFont(textFont)
        lbl6.setFont(textFont)

        valueFontS = QFont("Arial", 50)
        valueFontM = QFont("Arial", 100)
        valueFontL = QFont("Arial", 150)
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
        self.setGeometry(300, 300, 720, 480)
        self.setWindowTitle('Solar Car Dash')
        self.center()
        self.show()

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
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
            newMapName += str(int(newBatt / 100.0 * 24) + 1) + ".png"

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dash = Dashboard()
    sys.exit(app.exec_())