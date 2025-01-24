import os
import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv

from utils.constants import FROM_EMAIL, SMTP_PORT, SMTP_SERVER, SMTP_USERNAME

from .EmailService import EmailService

# Load environment variables from .env file
load_dotenv()


class SmtpEmailService(EmailService):
    smtp_server = SMTP_SERVER
    port = SMTP_PORT
    username = SMTP_USERNAME
    password = os.getenv("SMTP_PASSWORD")
    from_email = FROM_EMAIL

    @staticmethod
    def send_email(to: str, subject: str, body: str):
        """Send an email using the google SMTP Server."""
        # Create email message
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SmtpEmailService.from_email
        msg["To"] = to

        # Send the email
        try:
            with smtplib.SMTP(
                SmtpEmailService.smtp_server, SmtpEmailService.port
            ) as server:
                server.starttls()
                server.login(SmtpEmailService.username, SmtpEmailService.password)
                server.sendmail(SmtpEmailService.from_email, to, msg.as_string())
                print(f"Email sent to {to}")
        except Exception as e:
            print(f"Failed to send email: {e}")
