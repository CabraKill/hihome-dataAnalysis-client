import requests

from src.firestore.auth_error import AuthError


def read_value(document_id: str, token: str)-> str:
    link = "https://firestore.googleapis.com/v1/projects/home-dbb7e/databases/(default)/documents/unities/rft43A10RZ4LOmMQ6gry/sections/Y2OksEM7ErCqr2jx8UQJ/devices/{}".format(
        document_id)
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {}'.format(token)}
    firestore_request = requests.get(
        link, headers=headers)
    if firestore_request.status_code != 200:
        if(firestore_request.status_code == 401):
            raise AuthError(firestore_request.json(), firestore_request.status_code)
        raise Exception('failed to send temperature to firestore. Error: {}'.format(
            firestore_request.json()))
    value = firestore_request.json()['fields']['value']['stringValue']
    return value
    
