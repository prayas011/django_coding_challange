from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import generics
import license_portal

from license_portal.licenses.utils import send_license_notification_email
from .models import EmailLog  
from .serializers import EmailLogSerializer

class EmailLogList(generics.ListAPIView):
    queryset = EmailLog.objects.all()
    serializer_class = EmailLogSerializer

@csrf_exempt
def send_notifications(request):
    licenses_to_notify = license_portal.objects.get_licenses_to_notify()
    for license in licenses_to_notify:
        send_license_notification_email(license)
    return JsonResponse({"message": "Notifications sent"})

def get_recent_emails(request, num_emails):
    recent_logs = EmailLog.objects.all().order_by('-sent_at')[:num_emails]
    data = [{"sent_at": log.sent_at, "license_id": log.license_id} for log in recent_logs]
    return JsonResponse(data, safe=False)
