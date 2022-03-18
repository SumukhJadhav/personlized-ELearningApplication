import threading
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


db = firestore.client()
print('Connection initialized')

def update():
    doc_ref.update({u'country': "India"})



def on_snapshot(doc_snapshot, changes, read_time):
    count = 0
    for doc in doc_snapshot:
        print(u'Received document snapshot: {}'.format(doc.id))
        update();
doc_ref = db.collection('cities').document('LA')
doc_watch = doc_ref.on_snapshot(on_snapshot)
i=0 
import time           
while True:
    time.sleep(1)
    