from django.urls import path
from licenses.views import send_notifications
from licenses.views import get_recent_emails

urlpatterns = [
    path('send_notifications/', send_notifications, name='send_notifications'),
    path('get_recent_emails/<int:num_emails>/', get_recent_emails, name='get_recent_emails'),
]
