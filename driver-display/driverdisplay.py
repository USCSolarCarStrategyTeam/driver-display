from PyQt6.QtWidgets import (QWidget, QPushButton, QFrame, QColorDialog, QApplication, QLabel, QSplashScreen, )
from PyQt6.QtGui import QColor, QPainter, QFont, QPixmap
from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QTime, QTimer, QRectF
import sys
import os
import random
import time

updateTime = 1  # seconds


class Dashboard(QWidget):

    def __init__(self):
        super(Dashboard, self).__init__()

        self.initUI()

        self.timer = QTimer()
        self.timer.timeout.connect(self.getSpeed)
        self.timer.start(updateTime * 1000)

    def initUI(self):
        #setup variables
        self.lastSpeed = 0

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
        self.speedFrame.setGeometry(0, 0, 150, 130)
        self.speedFrame.setStyleSheet("""
            #speedFrame {
                border: 2px solid gold;
                border-radius: 10px;
            }
        """)

        lblSpeed = QLabel("Speed", self.speedFrame)
        lblSpeed.move(40, 5)
        lblSpeed.setFont(QFont("Arial", 20))
        lblSpeed.setStyleSheet(readingTitleSS)

        self.speedFrame.currSpeed = QLabel("0   ", self.speedFrame)
        self.speedFrame.currSpeed.move(40, 40)
        self.speedFrame.currSpeed.setFont(QFont("Arial", 50))
        self.speedFrame.currSpeed.setStyleSheet(valueSS)

        speedUnit = QLabel("mph", self.speedFrame)
        speedUnit.move(115, 110)
        speedUnit.setFont(QFont("Arial", 12))
        speedUnit.setStyleSheet(unitSS)

        # speed delta line
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

        # display a square for the speed delta
        speedDeltaContainer.diamond = QFrame(self.speedFrame.speedDeltaContainer)
        speedDeltaContainer.diamond.setObjectName("diamond")
        speedDeltaContainer.diamond.setGeometry(4, 46, 10, 10)
        speedDeltaContainer.diamond.setFrameShape(QFrame.Shape.Box)
        speedDeltaContainer.diamond.setLineWidth(2)
        speedDeltaContainer.diamond.setFrameShadow(QFrame.Shadow.Plain)

        # Setup Temperature display area
        self.tempFrame = QWidget(self)
        self.tempFrame.setObjectName("tempFrame")
        self.tempFrame.setGeometry(0, 130, 150, 350)
        self.tempFrame.setStyleSheet("""
            #tempFrame {
                border: 2px solid gold;
                border-radius: 10px;
            }
        """)

        lbl1t = QLabel("Temperatures", self.tempFrame)
        lbl1t.move(13, 5)
        lbl1t.setFont(QFont("Arial", 15))
        lbl1t.setStyleSheet(readingTitleSS)


        # Setup Power Display Area
        self.powerFrame = QWidget(self)
        self.powerFrame.setObjectName("powerFrame")
        self.powerFrame.setGeometry(520, 0, 200, 480)
        self.powerFrame.setStyleSheet("""
            #powerFrame {
                border: 2px solid gold;
                border-radius: 10px;
            }
        """)

        # Setup Battery Display Area
        self.batteryFrame = QWidget(self)
        self.batteryFrame.setObjectName("batteryFrame")
        self.batteryFrame.setGeometry(150, 380, 370, 100)
        self.batteryFrame.setStyleSheet("""
            #batteryFrame {
                border: 2px solid gold;
                border-radius: 10px;
            }
        """)




        # for making the dashboard fullscreen when env variable for FULLSCREEN is set to 1
        try:
            if os.environ["FULLSCREEN"] == "1":
                self.showFullScreen()
            else:
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

        newSpeed = random.uniform(50.0,55.0)
        self.speedFrame.currSpeed.setText(str(int(newSpeed)))

        acceleration = (newSpeed - self.lastSpeed) / updateTime # mph/s

        self.lastSpeed = newSpeed

        acceleration += 2.0
        if acceleration > 4.0:
            acceleration = 4.0
        elif acceleration < 0.0:
            acceleration = 0.0


        # calculate diamond position
        # +2mphs = 2 bars up
        # -2mphs = 2 bars down
        # 0mphs = center
        # 1 bar = 25px
        # +2mphs = 3px absolute
        # -2mphs = 97px absolute
        # 0mphs = 50px absolute
        y = 100.0-(acceleration * 25.0)-4.0
        self.speedFrame.speedDeltaContainer.diamond.setGeometry(4, int(y), 10, 10)



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
