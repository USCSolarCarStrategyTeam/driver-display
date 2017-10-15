

from IDriver import IInterface
import threading
import time


from random import randint
class Driver(IInterface):

    def __init__(self, RPMDriver): self.RPMDriver = RPMDriver

    def getRPM(self): return(self.RPMDriver.getRPM())
    def getBatteryTemperature(self,index): print (index)

class DummyRPMDriver():

    def getRPM(self):

        return randint(0,200);

class Dummy2RPMDriver():

    def getRPM(self): return 2;
