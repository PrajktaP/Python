from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('reminders/', include('reminders.urls')),
    path('notes/', include('notes.urls')),
]