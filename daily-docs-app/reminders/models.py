from django.db import models

class Reminder(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)  # Add this line
    notification_time = models.DateTimeField()  # Add this line
    remind_at = models.DateTimeField()
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title