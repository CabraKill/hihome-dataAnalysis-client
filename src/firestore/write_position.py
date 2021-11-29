import requests

from src.firestore.auth_error import AuthError
from src.position.position import Position


def write_position(document_id: str, position: Position, token: str):
    link = "https://firestore.googleapis.com/v1/projects/home-dbb7e/databases/(default)/documents/unities/rft43A10RZ4LOmMQ6gry/sections/Y2OksEM7ErCqr2jx8UQJ/devices/{}?updateMask.fieldPaths=point".format(
        document_id)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(token)
    }
    fields = {
        'fields': {
            'point': {
                'mapValue': {
                    'fields': {
                        'x': {
                            'doubleValue': position.x
                        },
                        'y': {
                            'doubleValue': position.y
                        }
                    }
                }
            }
        }
    }
    firestore_request = requests.patch(link, json=fields, headers=headers)
    if firestore_request.status_code != 200:
        if (firestore_request.status_code == 401):
            raise AuthError(firestore_request.json(),
                            firestore_request.status_code)
        raise Exception(
            'failed to write position to firestore. Error:\n {}'.format(
                firestore_request.json()))
