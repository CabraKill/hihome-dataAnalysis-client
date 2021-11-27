import requests


def get_token_from_firestore(email: str, password: str, key: str) -> str:
    response = requests.post('https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={}'.format(
        key), json={'email': email, 'password': password, 'returnSecureToken': True}, headers={'Content-Type': 'application/json'})
    if response.status_code != 200:
        raise Exception(
            'failed to login in firestore. Error: {}'.format(response.json()))
    token = response.json()['idToken']
    return token


if __name__ == '__main__':
    credentials = ('email', 'password', 'firestoreKey')
    token = get_token_from_firestore(credentials)
    print(token)
