import requests
import time


def send_value_to_ip(ip: str, value: str):
    start = time.time()
    response = requests.get(f'http://{ip}/RELAY={value.upper()}')
    flightTime = (time.time() - start) * 1000
    flightTimeString = str(flightTime)
    print(f'Flight time: {flightTimeString}')
    if response.status_code == 200:
        print(f'{value} sent to {ip}')
    else:
        raise SendValueError(
            f'Error sending value to {ip}. Error:\n {response.body}')


class SendValueError(Exception):
    message = ''

    def __init__(self, message):
        self.message = message