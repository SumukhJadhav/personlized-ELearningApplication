import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

import pyrebase
x = "s"
db = firestore.client()
data2 = {
    'name': 'Los Angeles',
    'state': 'CA',
    'country': 'UsSA'
}
data = {
    'name': 'Los Angeles',
    'state': 'CA',
    'country': 'UsSA',
    'objectExample': {
        'a': 5,
        'b': x
    }
}

# Add a new doc in collection 'cities' with ID 'LA'
#db.collection('cities').document('LAs').set(data)
# ------------------------------------------------------------

#Reading Documents
# doc_ref = db.collection(u'cities').document(u'LAs')
# doc = doc_ref.get()
# if doc.exists:
#     print(f'Document data: {doc.to_dict()}')
# else:
#     print(u'No such document!')

# ------------------------------------------------------------
#Updating Existing Doc
# ref = db.collection('cities').document('LAs')
# ref.update({u'country': "India"})

#Updating Nested Existing Doc
# ref = db.collection('cities').document('LAs')
# ref.update({u'objesctExample.a': "Ia"})

# ------------------------------------------------------------
#Delete Data
# db.collection(u'cities').document(u'LAs').delete()
# ------------------------------------------------------------



