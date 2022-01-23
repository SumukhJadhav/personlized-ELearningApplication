import pyrebase

firebase_config = {
    "apiKey": "AIzaSyBP3avv34HExit9IMtvLo2FrCXhcMoYrRo",
    "authDomain": "elearn-dfe88.firebaseapp.com",
    "databaseURL": "https://elearn-dfe88-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "projectId": "elearn-dfe88",
    "storageBucket": "elearn-dfe88.appspot.com",
    "messagingSenderId": "370909286054",
    "appId": "1:370909286054:web:ad7f2b2a17ba612b96ae67",
    "measurementId": "G-DSNXVDB2GQ"
}

firebase = pyrebase.initialize_app(firebase_config)

db = firebase.database()

data = {"name":"Sumukh","Age":19}
db.push(data)