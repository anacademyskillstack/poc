import os
import smtplib
from email.message import EmailMessage
from pathlib import Path


def send_html_email(
    to_email: str,
    subject: str,
    template_name: str,
    context: dict
):
    # Load HTML template
    template_path = Path("templates") / template_name
    html_content = template_path.read_text(encoding="utf-8")

    # Replace placeholders
    for key, value in context.items():
        html_content = html_content.replace(f"{{{{{key}}}}}", str(value))

    # Create email
    msg = EmailMessage()
    msg["From"] = os.getenv("EMAIL_USERNAME")
    msg["To"] = to_email
    msg["Subject"] = subject

    # VERY IMPORTANT:
    # 1️⃣ Plain-text fallback
    msg.set_content(
        "This is an HTML email. Please open it in an email client that supports HTML."
    )

    # 2️⃣ HTML version (this is what should render)
    msg.add_alternative(html_content, subtype="html")

    # Send
    with smtplib.SMTP(os.getenv("EMAIL_HOST"), int(os.getenv("EMAIL_PORT"))) as server:
        server.starttls()
        server.login(
            os.getenv("EMAIL_USERNAME"),
            os.getenv("EMAIL_PASSWORD")
        )
        server.send_message(msg)
