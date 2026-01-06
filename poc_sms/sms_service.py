from twilio.rest import Client
from config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER
)

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms(phone: str, message: str):
    message = client.messages.create(
        body=message,
        from_=+12272573330,
        to=phone
    )
    return message.sid
