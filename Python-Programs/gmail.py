import smtplib
from email.message import EmailMessage
import os
import time
from datetime import datetime

def send_email_using_gmail(attachment, receiver, email_body):
    # Email content setup
    msg = EmailMessage()
    msg['Subject'] = f"File Logs | {datetime.now().strftime("%Y%m%d")}"
    msg['From'] = 'prajktappp03@gmail.com'
    msg['To'] = receiver
    msg.set_content(email_body)

    # File attachment
    file_path = attachment
    file_name = os.path.basename(file_path)

    f = open(file_path, 'r')
    file_content = f.read()
    try:
        msg.add_attachment(file_content, subtype='plain', filename=file_name)
    
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('prajktappp03@gmail.com', 'eock ehjw bshg kcyj')  # Use app password if 2FA is enabled
            smtp.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)
