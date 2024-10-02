# users/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

def send_password_email_task(email, password):
    subject = "Your Login Password"
    message = f"Hello, you just logged in. Your password is: {password}"
    from_email = settings.DEFAULT_FROM_EMAIL  # Use from_email from settings

    # Send the email
    try:
        send_mail(subject, message, from_email, [email], fail_silently=False)
        return "Email sent successfully"
    except Exception as e:
        print(f"Email sending failed: {str(e)}")
        return f"Email sending failed: {str(e)}"
