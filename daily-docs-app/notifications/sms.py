from twilio.rest import Client

def send_sms_notification(to_number, message, from_number, account_sid, auth_token):
    client = Client(account_sid, auth_token)
    client.messages.create(
        to=to_number,
        from_=from_number,
        body=message
    )