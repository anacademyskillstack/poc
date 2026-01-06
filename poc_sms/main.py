from fastapi import FastAPI
from pydantic import BaseModel
from sms_service import send_sms

app = FastAPI()

class SMSRequest(BaseModel):
    phone_number: str
    message: str

@app.post("/send-sms")
def send_sms_api(data: SMSRequest):
    sid = send_sms(data.phone_number, data.message)
    return {"status": "sent", "sid": sid}
