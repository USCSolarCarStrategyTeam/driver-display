from driver.Driver import Driver
from driver.Driver import Dummy2RPMDriver

c = Driver(Dummy2RPMDriver())
print(c.getRPM())