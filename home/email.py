from django.core.mail import EmailMessage
from django.conf import settings


def send_my_email(message):
    adminEmail = 'alexanderemmanuel1719@gmail.com'
    subject = 'ALEXIS DELIVERY'
    email_message = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [adminEmail],
    )
    if email_message.send():
        return True
    else:
        return False
