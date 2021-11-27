from src.firestore.auth_error import AuthError
from src.login.login import login
from src.temperature.read import read_temperature
from src.firestore.send_temperature import send_temperatue
import time
DELAY = 2


def main():
    temperature_sensor_list = [
        ('GPU Core', 'kwSEFDDv2C5P9X2qs5dI'), ('CPU Core #1', '9nCNhqpGGsIE30vL7fRF'), ('CPU Core #2', 'ePyuDpVex2sFUcfulBMY')]
    token = login()
    sensor_dict = {}
    while True:
        last_temperature = None
        changed = False
        for sensor in temperature_sensor_list:
            try:
                sensor_name = sensor[0]
                document_id = sensor[1]
                temperature = read_temperature(sensor_name)
                if(temperature == sensor_dict.get(sensor_name)):
                    break
                changed = False
                send_temperatue(document_id, temperature, token)
                sensor_dict[sensor_name] = temperature
                print("{} - temp {} ºC".format(sensor_name, temperature))
            except AuthError as e:
                token = login(use_cache = False)
            except Exception as e:
                print("Error: {}".format(e))
            if(changed):
                time.sleep(2)   


if __name__ == '__main__':
    main()
