# This class is responsible for sending notifications with the deal flight details.
from decouple import config
from twilio.rest import Client
from twilio.rest.api.v2010.account import message

ACCOUNT_SID = config('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN')
MY_PHONE_NUMBER = config('MY_PHONE_NUMBER')


class NotificationManager:
    def __init__(self, twilio_sid=ACCOUNT_SID, twilio_auth_token=TWILIO_AUTH_TOKEN, twilio_phone_number=MY_PHONE_NUMBER) -> str:
        self.sid = twilio_sid
        self.auth_token = twilio_auth_token
        self.from_phone_number = twilio_phone_number
        # self.message()

    def send(self):
        print(f'SID {ACCOUNT_SID}\nfrom number{self.from_phone_number}')
        # client = Client(self.sid, self.auth_token)
        # message = client.messages \
        #     .create(
        #         body="Hi Daniel Poop Face Gomes",
        #         from_=self.from_phone_number,
        #         to=self.from_phone_number
        #     )
        # print(message.id)
