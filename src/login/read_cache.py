import os

from src.cache.read_cache import readFromFile


def getTokenIfCacheExists():
    FILE_NAME = "token.txt"
    text = readFromFile(FILE_NAME)
    return text


def getEmailIfCacheExists():
    FILE_NAME = "email.txt"
    text = readFromFile(FILE_NAME)
    return text


def getPasswordIfCacheExists():
    FILE_NAME = "password.txt"
    text = readFromFile(FILE_NAME)
    return text

def getKeyIfCacheExists():
    FILE_NAME = "key.txt"
    text = readFromFile(FILE_NAME)
    return text


if __name__ == "__main__":
    token = getTokenIfCacheExists()
    print(token)
