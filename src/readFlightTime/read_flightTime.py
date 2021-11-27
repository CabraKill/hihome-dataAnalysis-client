from dateutil import parser
import requests

from src.firestore.auth_error import AuthError
from src.readFlightTime.models.flight import Flight
from datetime import datetime

from src.write_flight_time_cache.write_flight_time_cache import writeFlightHour, writeFlightTime, writeFlightTotal


def read_flightTime(document_id: str, token: str):
    link = "https://firestore.googleapis.com/v1/projects/home-dbb7e/databases/(default)/documents/unities/rft43A10RZ4LOmMQ6gry/sections/Y2OksEM7ErCqr2jx8UQJ/devices/{}/flightTime?pageSize=1000".format(
        document_id)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(token)
    }
    firestore_request = requests.get(link, headers=headers)
    if firestore_request.status_code != 200:
        if (firestore_request.status_code == 401):
            raise AuthError(firestore_request.json(),
                            firestore_request.status_code)
        raise Exception(
            'failed to send temperature to firestore. Error: {}'.format(
                firestore_request.json()))
    print("statusCode: " + str(firestore_request.status_code))
    json = firestore_request.json()
    flightList = []
    flightListString = []
    for document in json['documents']:
        time = str(document['fields']['time']['doubleValue'])
        date = str(document['createTime'])
        # 2021-11-26T01: 35: 08.208796Z
        # flight = Flight(time, datetime.strptime(date, "%Y-%m-%dT%I:%M:%S"))
        flight = Flight(time,
                        datetime.fromtimestamp(parser.parse(date).timestamp()))
        flightList.append(flight)
    flightList.sort(key=lambda x: x.date)
    writeFlightTime(flightList)
    writeFlightHour(flightList)
    writeFlightTotal(flightList)
    # with open("flightTime.txt", "w") as f:
    #     for flight in flightList:
    #         together = flight.time + " " + str(flight.date)
    #         flightListString.append(together)
    #         f.write(flight.time + "\n")
    # with open("flightTime-hour.txt", "w") as f:
    #     for flight in flightList:
    #         formattedDate = flight.date.strftime("%H:%M:%S")
    #         f.write(formattedDate + "\n")
    # with open("flightTime-total.txt", "w") as f:
    #     for flight in flightListString:
    #         print(flight)
    #         f.write(flight + "\n")

    return firestore_request.json()
