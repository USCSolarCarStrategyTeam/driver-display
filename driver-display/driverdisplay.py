from PyQt6.QtWidgets import (QWidget,QPushButton, QFrame, QColorDialog, QApplication, QLabel, QSplashScreen,)
from PyQt6.QtGui import QColor, QPainter, QFont, QPixmap
from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QTime, QTimer, QRectF
import sys
import os
from random import randint
import time

class Dashboard(QWidget):

    def __init__(self):
        super(Dashboard, self).__init__()

        self.initUI()

        self.speedTimer = QTimer()
        self.speedTimer.timeout.connect(self.getSpeed)
        self.speedTimer.start(500)  # every 1 second,

        self.motorTempTimer = QTimer()
        self.motorTempTimer.timeout.connect(self.getMotorTemp)
        self.motorTempTimer.start(500) #every second

        self.cabinTempTimer = QTimer()
        self.cabinTempTimer.timeout.connect(self.getCabinTemp)
        self.cabinTempTimer.start(500)  # every second

    def initUI(self):
        # Configure colors
        readingTitleSS = "QLabel { color: gold; }"
        unitSS = "QLabel { color: grey; }"
        valueSS = "QLabel { color: white; }"

        background = QColor(50, 50, 50)  # dark grey to not blind the driver

        # Create Viewport
        self.setGeometry(0, 0, 720, 480)
        self.center()
        self.setWindowTitle('Solar Car Dash')

        # setup dashboard background
        p = self.palette()
        p.setColor(self.backgroundRole(), background)
        self.setPalette(p)

        # Setup Speed display area

        self.speedFrame = QWidget(self)
        self.speedFrame.setObjectName("speedFrame")
        self.speedFrame.setGeometry(1, 1, 150, 130)
        self.speedFrame.setStyleSheet("""
            #speedFrame {
                border: 2px solid gold;
                border-radius: 10px;
            }
        """)

        lbl1 = QLabel("Speed", self.speedFrame)
        lbl1.move(40, 5)
        lbl1.setFont(QFont("Arial", 20))
        lbl1.setStyleSheet(readingTitleSS)

        self.speedFrame.currSpeed = QLabel("0   ", self.speedFrame)
        self.speedFrame.currSpeed.move(40, 40)
        self.speedFrame.currSpeed.setFont(QFont("Arial", 50))
        self.speedFrame.currSpeed.setStyleSheet(valueSS)

        speedUnit = QLabel("mph", self.speedFrame)
        speedUnit.move(115, 110)
        speedUnit.setFont(QFont("Arial", 12))
        speedUnit.setStyleSheet(unitSS)

        #speed delta line
        self.speedFrame.speedDeltaContainer = QWidget(self.speedFrame)
        speedDeltaContainer = self.speedFrame.speedDeltaContainer
        speedDeltaContainer.setObjectName("speedDeltaContainer")
        speedDeltaContainer.setGeometry(10, 15, 20, 103)
        speedDeltaContainer.setStyleSheet("""
            #markers {
                color: white;
            }
            #vBar {
                color: white;
            }
            #diamond {
                color: white;
            }
        """)

        speedDeltaContainer.vBar = QFrame(self.speedFrame.speedDeltaContainer)
        speedDeltaContainer.vBar.setObjectName("vBar")
        speedDeltaContainer.vBar.setGeometry(8, 0, 3, 100)
        speedDeltaContainer.vBar.setFrameShape(QFrame.Shape.VLine)
        speedDeltaContainer.vBar.setLineWidth(2)

        speedDeltaContainer.marker1 = QFrame(self.speedFrame.speedDeltaContainer)
        speedDeltaContainer.marker1.setObjectName("markers")
        speedDeltaContainer.marker1.setGeometry(4, 0, 10, 3)
        speedDeltaContainer.marker1.setFrameShape(QFrame.Shape.HLine)
        speedDeltaContainer.marker1.setLineWidth(2)

        speedDeltaContainer.marker2 = QFrame(self.speedFrame.speedDeltaContainer)
        speedDeltaContainer.marker2.setObjectName("markers")
        speedDeltaContainer.marker2.setGeometry(4, 25, 10, 3)
        speedDeltaContainer.marker2.setFrameShape(QFrame.Shape.HLine)
        speedDeltaContainer.marker2.setLineWidth(2)

        speedDeltaContainer.marker3 = QFrame(self.speedFrame.speedDeltaContainer)
        speedDeltaContainer.marker3.setObjectName("markers")
        speedDeltaContainer.marker3.setGeometry(4, 50, 10, 3)
        speedDeltaContainer.marker3.setFrameShape(QFrame.Shape.HLine)
        speedDeltaContainer.marker3.setLineWidth(2)

        speedDeltaContainer.marker4 = QFrame(self.speedFrame.speedDeltaContainer)
        speedDeltaContainer.marker4.setObjectName("markers")
        speedDeltaContainer.marker4.setGeometry(4, 75, 10, 3)
        speedDeltaContainer.marker4.setFrameShape(QFrame.Shape.HLine)
        speedDeltaContainer.marker4.setLineWidth(2)

        speedDeltaContainer.marker5 = QFrame(self.speedFrame.speedDeltaContainer)
        speedDeltaContainer.marker5.setObjectName("markers")
        speedDeltaContainer.marker5.setGeometry(4, 100, 10, 3)
        speedDeltaContainer.marker5.setFrameShape(QFrame.Shape.HLine)
        speedDeltaContainer.marker5.setLineWidth(2)

        # display a square and rotate it 45 degrees to make a diamond
        speedDeltaContainer.diamond = QFrame(self.speedFrame.speedDeltaContainer)
        speedDeltaContainer.diamond.setObjectName("diamond")
        speedDeltaContainer.diamond.setGeometry(4, 46, 10, 10)
        speedDeltaContainer.diamond.setFrameShape(QFrame.Shape.Box)
        speedDeltaContainer.diamond.setLineWidth(2)
        speedDeltaContainer.diamond.setFrameShadow(QFrame.Shadow.Plain)

        #Setup Temperature display area

        #making the temps box
        self.tempFrame = QWidget(self)
        self.tempFrame.setObjectName("tempFrame")
        self.tempFrame.setGeometry(1, 130, 150, 350)
        self.tempFrame.setStyleSheet("""
                    #tempFrame {
                        border: 2px solid gold;
                        border-radius: 10px;
                    }
                """)

        #"Temperatures" label
        lbl1t = QLabel("Temperatures", self.tempFrame)
        lbl1t.move(13, 5)
        lbl1t.setFont(QFont("Arial", 15))
        lbl1t.setStyleSheet(readingTitleSS)

        #motor temperature
        motorTempLabel = QLabel("Motor: ", self.tempFrame)
        motorTempLabel.move(45, 35)
        motorTempLabel.setFont(QFont("Arial", 15))
        motorTempLabel.setStyleSheet(readingTitleSS)

        self.tempFrame.currMotorTemp = QLabel("0   ", self.tempFrame)
        self.tempFrame.currMotorTemp.move(40, 60)
        self.tempFrame.currMotorTemp.setFont(QFont("Arial", 30))
        self.tempFrame.currMotorTemp.setStyleSheet(valueSS)

        motorTempUnit = QLabel("C", self.tempFrame)
        motorTempUnit.move(115, 80)
        motorTempUnit.setFont(QFont("Arial", 12))
        motorTempUnit.setStyleSheet(unitSS)

        #cabin temperature
        cabinTempLabel = QLabel("Cabin: ", self.tempFrame)
        cabinTempLabel.move(45, 110)
        cabinTempLabel.setFont(QFont("Arial", 15))
        cabinTempLabel.setStyleSheet(readingTitleSS)

        self.tempFrame.currCabinTemp = QLabel("0   ", self.tempFrame)
        self.tempFrame.currCabinTemp.move(40, 135)
        self.tempFrame.currCabinTemp.setFont(QFont("Arial", 30))
        self.tempFrame.currCabinTemp.setStyleSheet(valueSS)

        motorTempUnit = QLabel("C", self.tempFrame)
        motorTempUnit.move(115, 155)
        motorTempUnit.setFont(QFont("Arial", 12))
        motorTempUnit.setStyleSheet(unitSS)

        # for making the dashboard fullscreen when env variable for FULLSCREEN is set to 1
        try:
            if os.environ["FULLSCREEN"] == "1":
                self.showFullScreen()
            else :
                self.show()
        except:
            self.show()

    # pressing escape closes the window
    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_Escape:
            self.close()

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def getSpeed(self):

        # TODO: replace with actual data read from database

        newSpeed = randint(50, 59)
        self.speedFrame.currSpeed.setText(str(newSpeed))

    def getMotorTemp(self):

        # TODO: replace with actual data

        newMotorTemp = randint(0, 100)
        self.tempFrame.currMotorTemp.setText(str(newMotorTemp))

    def getCabinTemp(self):

        # TODO: replace with actual data

        newCabinTemp = randint(0, 100)
        self.tempFrame.currCabinTemp.setText(str(newCabinTemp))




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
