from src.firestore.auth_error import AuthError
from src.login.login import login
from src.temperature.read import read_temperature
from src.firestore.send_temperature import send_temperatue
from src.readFlightTime.read_flightTime import read_flightTime


def main():
    token = login()
    while True:
        try:
            read_flightTime("xC8UGLSYT8z2pxwKaAeY", token)
            break
        except AuthError as e:
            token = login(use_cache=False)  
        except Exception as e:
            # "time data '2021-11-26T01:33:58.825320Z' does not match format '%Y-%m-%dT%I:%M:%S'"
            print("Error: {}".format(e))
            break


if __name__ == '__main__':
    main()
