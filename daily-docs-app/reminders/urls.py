from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminder_list, name='reminder_list'),
    path('add/', views.reminder_add, name='reminder_add'),
    path('edit/<int:id>/', views.reminder_edit, name='reminder_edit'),
    path('delete/<int:id>/', views.reminder_delete, name='reminder_delete'),
]