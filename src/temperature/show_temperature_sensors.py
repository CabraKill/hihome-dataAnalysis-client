# https://stackoverflow.com/questions/3262603/accessing-cpu-temperature-in-python

import wmi
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
temperature_infos = w.Sensor()
for sensor in temperature_infos:
    if sensor.SensorType==u'Temperature':
        print(sensor.Name)
        print(sensor.Value)