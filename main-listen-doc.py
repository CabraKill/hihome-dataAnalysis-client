import threading
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from datetime import datetime
from src.device_requests.send_value import SendValueError, send_value_to_ip

call_back = threading.Event()
ip = ''


def printDoc(col_snapshot, changes, read_time):
    for doc in col_snapshot:
        try:
            # now = time.time()
            dt = datetime.now()
            second = dt.second
            nowMili = dt.microsecond / 1000
            print(
                # f'seconds from python: {time.strftime("%S")} micro: {time.strftime("%f")}'
                f'seconds from python: {second} micro: {nowMili}')
            print(f'seconds from firestore: {read_time.second} micro: {read_time.microsecond}')
            value = doc.get("value")
            print(f'{value}')
            ip = doc.get("ip")
            if ip:
                send_value_to_ip(ip, value)
        except SendValueError as e:
            print(e.message)
        except Exception as e:
            ip = ''
            print(f'Error: {e}')
    call_back.set()


firCredentials = credentials.Certificate("firebase.json")
firApp = firebase_admin.initialize_app(firCredentials)

db = firestore.client()

doc = db.document(
    u'unities/rft43A10RZ4LOmMQ6gry/sections/Y2OksEM7ErCqr2jx8UQJ/devices/xC8UGLSYT8z2pxwKaAeY'
)

query_watch = doc.on_snapshot(printDoc)
call_back.wait()
print('Press Ctrl+C to exit <3')
while True:
    pass
query_watch.unsubscribe()
