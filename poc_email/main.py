from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from email_service import send_html_email

load_dotenv()

app = FastAPI(title="Email POC")

class EmailRequest(BaseModel):
    to_email: str
    name: str
    email: str
    address: str
    appointment_date: str
    report_time: str

@app.post("/send-email")
def send_email_api(data: EmailRequest):
    send_html_email(
        to_email=data.to_email,
        subject="Appointment Confirmation",
        template_name="welcome_email.html",
        context={
            "name": data.name,
            "email": data.email,
            "address": data.address,
            "appointment_date": data.appointment_date,
            "report_time": data.report_time
        }
    )
    return {"message": "HTML email sent successfully"}
