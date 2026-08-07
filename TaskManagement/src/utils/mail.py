from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import BaseModel, EmailStr
from typing import List

conf = ConnectionConfig(
    MAIL_USERNAME = "alastermoody962@email.com",
    MAIL_PASSWORD = "kkjd fijo ozvh qmki",
    MAIL_FROM = "alastermoody962@email.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="Task Management",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

async def send_mail(emails: List[str]):
    html = """<p>Hi, thanks for registering, Feel free to connect with us anytime!</p> """

    message = MessageSchema(
        subject="Registration Confirmation",
        recipients=emails,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return { "success": True, "message": "Mail sent successfully" }