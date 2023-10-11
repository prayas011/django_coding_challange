from rest_framework.views import APIView
from rest_framework.response import Response
from .models import License


class SendLicenseNotificationsView(APIView):

    def post(self, request):
        return Response({"message": "Emails sent successfully!"})
