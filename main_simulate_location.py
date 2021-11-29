from src.firestore.auth_error import AuthError
from src.firestore.write_position import write_position
from src.login.login import login
from src.temperature.read import read_temperature
from src.firestore.send_temperature import send_temperatue
import time
from src.position.generatePoints import generatePoints

from src.position.position import Position

DELAY = 2
DEVICE_ID = ''
POINTS = [
    Position(0, 0),
    Position(0, 0.95),
    Position(0.95, 0.95),
    Position(0.95, 0),
    Position(0, 0)
]

PRECISION = 10

DEVICE_ID = 'QqvMGp7yZZvzgqxdt56F'


def main():
    token = login()
    currentPointIndex = 0
    pointList = generatePoints(POINTS, PRECISION)
    while True:
        try:
            if currentPointIndex >= len(pointList):
                currentPointIndex = 0
            newLocation = pointList[currentPointIndex]
            print("x: {} y: {}".format(newLocation.x, newLocation.y))
            write_position(DEVICE_ID, newLocation, token)
            currentPointIndex += 1
        except AuthError as e:
            token = login(use_cache=False)
        except Exception as e:
            print("Error: {}".format(e))
        time.sleep(1.5)


if __name__ == '__main__':
    main()
