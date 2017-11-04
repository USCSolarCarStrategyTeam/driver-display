from abc import ABCMeta, abstractmethod

class IInterface:
    __metaclass__ = ABCMeta
    @abstractmethod
    def getBatteryTemperature(self,index): raise NotImplementedError

    @abstractmethod
    def getRPM(self): raise NotImplementedError

    @abstractmethod
    def getConnection(self): raise NotImplementedError




