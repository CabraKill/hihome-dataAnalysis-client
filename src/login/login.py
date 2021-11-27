from src.firestore.get_token import get_token_from_firestore
from src.login.credentials_read import get_credentials
from src.login.write_cache import write_key, write_token, write_email, write_password
from src.login.read_cache import getEmailIfCacheExists, getKeyIfCacheExists, getPasswordIfCacheExists, getTokenIfCacheExists


def login(use_cache: bool = True) -> str:
    if(getTokenIfCacheExists() and use_cache):
        token = getTokenIfCacheExists()
    else:
        email = getEmailIfCacheExists()
        if email != None:
            password = getPasswordIfCacheExists() 
            key = getKeyIfCacheExists()
            save_credentials = "y"
        else:
            credentials = get_credentials()
            email = credentials[0]
            password = credentials[1]
            key = credentials[2]
            save_credentials = input("Do you want to save the credentials? (y/n)")
        try:
            token = get_token_from_firestore(email, password, key)
            if(save_credentials == "y"):
                write_email(email)
                write_password(password)
                write_token(token)
                write_key(key)
        except Exception as e:
            return None
    return token


if __name__ == '__main__':
    token = login()
    print(token)
