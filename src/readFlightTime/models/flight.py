from datetime import datetime

class Flight:
    time = ''
    date = datetime.now();
    def __init__(self, time: str, date: datetime) -> None:
        self.time = time
        self.date = date