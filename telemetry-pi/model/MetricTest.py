#from Metric import Metric
import jsonpickle
from BatteryTemperature import BatteryTemperature
from MetricType import MetricType
from Voltage import Voltage
from RPM import RPM

tempBattery0 = BatteryTemperature(MetricType.BATTERY,100, 0)
tempBattery1 = BatteryTemperature(MetricType.BATTERY,100, 1)
tempBattery2 = BatteryTemperature(MetricType.BATTERY,100, 2)
voltBattery = Voltage(MetricType.BATTERY, 150)
voltSolarCell =  Voltage(MetricType.SOLAR_CELL, 75)
rpm = RPM(MetricType.RPM,200)

print (jsonpickle.encode(tempBattery0))
result = jsonpickle.decode('{"py/object": "BatteryTemperature.BatteryTemperature", "index": 0, "name": {"py/reduce": [{"py/type": "MetricType.MetricType"}, {"py/tuple": ["battery"]}, null, null, null]}, "value": 100}')
print (result.index, result.name)

print (jsonpickle.encode(voltBattery))
print (jsonpickle.encode(voltSolarCell))
print (jsonpickle.encode(rpm))
