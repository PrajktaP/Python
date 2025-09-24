def send_email_notification(subject, message, recipient_list):
    from django.core.mail import send_mail
    from django.conf import settings

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False,
    )

def send_sms_notification(phone_number, message):
    # Placeholder for SMS sending logic
    # This function should integrate with an SMS service provider
    pass

def format_notification_message(task_name, due_date):
    return f"Reminder: The task '{task_name}' is due on {due_date}."