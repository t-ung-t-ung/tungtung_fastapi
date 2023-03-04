import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred_path = "hyu-around-firebase-adminsdk-hwbpd-acbbacf5a4.json"
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

# 이 토큰을 프론트에서 줘야 되는 것 같다... 아마도...
registration_token = 'cBPtDKvuSBK1C7jsu9j5Tk:APA91bE52VQRECUCAILH4XVmLcmMuISbV9QTHZgr3II_03cbuSha9a-MBl5xgop9jlQ6-tSdBRumj5zu8pdwCgvK2ySQXt-RMTQveK34pQjSePRf8TkBtrKDpRK6r27dpPzwA0pSSLIM'
message = messaging.Message(
    notification=messaging.Notification(
        title='title',
        body='body'
    ),
    token=registration_token,
)

response = messaging.send(message)
print('Successfully sent message:', response)
