# python script to send an email automatically

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # TLS protocol, default for security

def send_from_joelbot(email_user: str, email_password: str, recipient: str, subject: str, html_body: str) -> None:
    """Send a message from joelbot404@gmail.com to recipient, specifying subject and body."""
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(html_body, 'html'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(email_user, email_password)
        text = msg.as_string()
        server.sendmail(email_user, recipient, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email due to error: {e}")
    finally:
        server.quit()
