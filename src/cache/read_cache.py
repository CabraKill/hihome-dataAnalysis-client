import os

def readFromFile(file_name: str):
    if not os.path.isfile(file_name):
        return None
    cache_file = open(file_name, "r")
    text = cache_file.read()
    if text == "":
        return None
    else:
        return text