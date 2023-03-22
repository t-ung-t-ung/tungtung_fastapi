import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred_path = "firebase/hyu-around-firebase-adminsdk-hwbpd-acbbacf5a4.json"
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

# 이 토큰을 프론트에서 줘야 되는 것 같다... 아마도...


def send_message(fcm_token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        token=fcm_token,
    )

    response = messaging.send(message)
    print('Successfully sent message:', response)
