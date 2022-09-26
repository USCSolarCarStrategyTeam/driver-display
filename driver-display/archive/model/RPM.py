from Metric import Metric
class RPM(Metric):
    def __init__(self, name, value):
        Metric.__init__(self, name)
        self.value = value
