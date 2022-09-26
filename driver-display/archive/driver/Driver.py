import IDriver

from random import randint


class Driver(IDriver.IInterface):

    def __init__(self, RPMDriver): self.RPMDriver = RPMDriver

    def getRPM(self): return self.RPMDriver.getRPM()

    def getBatteryTemperature(self, index): print(index)

    def getConnection(self): return self.RPMDriver.getConnection()


class DummyRPMDriver:

    def getRPM(self):
        return randint(0, 200);


class Dummy2RPMDriver():

    def getRPM(self): return 2;


class DummyConnectedDriver():

    def getConnection(self):
        return randint(0, 1);
