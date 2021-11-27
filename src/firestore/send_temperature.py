import requests

from src.firestore.auth_error import AuthError


def send_temperatue(document_id: str, temp: float, token: str):
    link = "https://firestore.googleapis.com/v1/projects/home-dbb7e/databases/(default)/documents/unities/rft43A10RZ4LOmMQ6gry/sections/Y2OksEM7ErCqr2jx8UQJ/devices/{}?updateMask.fieldPaths=value".format(
        document_id)
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {}'.format(token)}
    firestore_request = requests.patch(
        link, json={'fields': {'value': {'stringValue': str(temp)}}}, headers=headers)
    if firestore_request.status_code != 200:
        if(firestore_request.status_code == 401):
            raise AuthError(firestore_request.json(), firestore_request.status_code)
        raise Exception('failed to send temperature to firestore. Error: {}'.format(
            firestore_request.json()))
    
