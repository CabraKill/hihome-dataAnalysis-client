# https://stackoverflow.com/questions/3262603/accessing-cpu-temperature-in-python

import wmi


def read_temperature(sensor_name: str) -> float:
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    temperature_infos = w.Sensor()
    temperature = None
    for sensor in temperature_infos:
        if sensor.SensorType == 'Temperature' and sensor.Name == sensor_name:
            temperature = sensor.Value
            break
    if(temperature != None):
        return temperature
    raise Exception("No temperature sensor found for {}".format(sensor_name))


if __name__ == "__main__":
    print('From function: ' + str(read_temperature()))
