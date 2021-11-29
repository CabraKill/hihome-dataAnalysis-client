from src.device_requests.send_value import send_value_to_ip
from src.firestore.auth_error import AuthError
from src.firestore.read_value import read_value
from src.login.login import login
from src.readFlightTime.models.flight import Flight
import time
from datetime import datetime

from src.write_flight_time_cache.write_flight_time_cache import writeFlightHour, writeFlightTime, writeFlightTotal


def main():
    token = login()
    flightList = []
    count = 0
    while True:
        try:
            if count == 150:
                break
            start = time.time()
            send_value_to_ip("192.168.0.99", 'on')
            flightTime = (time.time() - start) * 1000
            flightTimeString = str(flightTime)
            print("Flight time: {}".format(flightTimeString))
            dateNow = datetime.today()
            flight = Flight(flightTimeString, dateNow)
            flightList.append(flight)
            count += 1
        except AuthError as e:
            token = login(use_cache=False)  
        except Exception as e:
            print("Error: {}".format(e))
            break
    writeFlightTime(flightList)
    writeFlightHour(flightList)
    writeFlightTotal(flightList)


if __name__ == '__main__':
    main()
