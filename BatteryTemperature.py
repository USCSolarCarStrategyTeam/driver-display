from Temperature import Temperature
class BatteryTemperature(Temperature):
    def __init__(self, name, value, index):
        Temperature.__init__(self, name, value)
        self.index = index
