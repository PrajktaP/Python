from django.shortcuts import render, redirect
from .models import Reminder
from .forms import ReminderForm

def reminder_list(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminders/reminder_list.html', {'reminders': reminders})

def reminder_add(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reminders:reminder_list')
    else:
        form = ReminderForm()
    return render(request, 'reminders/reminder_form.html', {'form': form})

def reminder_update(request, pk):
    reminder = Reminder.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('reminders:reminder_list')
    else:
        form = ReminderForm(instance=reminder)
    return render(request, 'reminders/reminder_form.html', {'form': form})

def reminder_delete(request, pk):
    reminder = Reminder.objects.get(pk=pk)
    if request.method == 'POST':
        reminder.delete()
        return redirect('reminders:reminder_list')
    return render(request, 'reminders/reminder_confirm_delete.html', {'reminder': reminder})

def reminder_edit(request, pk):
    return reminder_update(request, pk)