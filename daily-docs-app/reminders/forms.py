from django import forms
from .models import Reminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'description', 'notification_time']  # Adjust fields as per your Reminder model
        widgets = {
            'notification_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }