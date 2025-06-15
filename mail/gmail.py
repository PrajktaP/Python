import smtplib
from email.message import EmailMessage
import os

def send_email_using_gmail(attachment, receiver):
    # Email content setup
    msg = EmailMessage()
    msg['Subject'] = 'File Deletion Logs'
    msg['From'] = 'something@gmail.com'
    msg['To'] = receiver
    msg.set_content('Please find the attachment.')

    # File attachment
    file_path = attachment
    file_name = os.path.basename(file_path)

    f = open(file_path, 'r')
    file_content = f.read()
    try:
        msg.add_attachment(file_content, subtype='plain', filename=file_name)
    
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('something@gmail.com', 'your app pwd')  # Use app password if 2FA is enabled
            smtp.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)
