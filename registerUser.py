import pymongo
import dns
import random
from twilio.rest import Client
import string
import re

def signup():
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  

    def passcheck(s):
        if len(list(set(s)&set(string.ascii_lowercase)))>0 and len(list(set(s)&set(string.ascii_uppercase)))>0 and len(list(set(s)&set(string.digits)))>0 and len(list(set(s)&set(string.punctuation)))>0:
            return "Strong"
        else: return "Weak"

    otp = random.randint(1000,9999)
    account_sid = 'xxxx'
    auth_token = 'xxxx'

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    mail = input("Enter Email: ")
    username = input("Enter Username: ")
    if(re.search(regex,mail)):   
            pass 

    phno = int(input("Enter 10 digit Phone Number: "))


    client = Client(account_sid, auth_token)
    msg = client.messages.create(
        body = f'Hello {name}, your OTP for Fiqlo signup is {otp}',
        from_ = '+xxxx',
        to = f'+91{phno}'
        )
    print(f'OTP sent to {phno}')
    otp2 = int(input(f"Enter OTP sent to {phno} : "))

    if otp2 == otp:
        print("Phone Number successfully verified")
    else:
        print("OTP invalid, type number again.breakakak")

    password  = input("Enter a password: ")
    if passcheck(password) == 'Strong':
        password2 = input("Enter password again: ")
        if password2 == password:
            print("Password set successfully!")
            print("Happy Learning")
    else:
        print("Weak Password. blacjfjss")


    clients = pymongo.MongoClient("mongodb+srv://xxxx:xxxxe@cluster78.nyeu3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = clients.test

    col = db['test1']


    dic = {'name':f'{name}','Age':age,'Phone':phno,'Username':username, 'Passcode': password}
    x = col.insert_one(dic)
    #print(x)

    #print((col.find_one({'Age':21})))

signup()
    



