from django.contrib import admin
from datetime import datetime, timedelta
from licenses.models import License, Client, EmailLog  # Assuming EmailLog model exists
from django.core.mail import send_mail


def prepare_email_body(client_licenses):
    """Prepare the body of the email with license details."""
    email_content = []

    for license_obj in client_licenses:
        details = f"""
        License ID: {license_obj.id}
        License Type: {license_obj.license_type}
        Package Name: {license_obj.package_name}
        Expiration Date: {license_obj.expiration_date}
        POC Name: {license_obj.client.admin_poc.name}
        POC Email: {license_obj.client.admin_poc.email}
        """
        email_content.append(details)

    return "\n\n".join(email_content)


def send_expiry_notifications():
    # Fetching licenses based on expiry criteria
    today = datetime.now()
    four_months_from_now = today + timedelta(days=120)
    one_month_from_now = today + timedelta(days=30)
    one_week_from_now = today + timedelta(days=7)

    licenses_in_four_months = License.objects.filter(expiration_date=four_months_from_now)
    licenses_in_one_month = License.objects.filter(expiration_date__lte=one_month_from_now) if today.weekday() == 0 else []
    licenses_in_one_week = License.objects.filter(expiration_date__lte=one_week_from_now)

    all_filtered_licenses = set(licenses_in_four_months) | set(licenses_in_one_month) | set(licenses_in_one_week)

    for client in Client.objects.all():
        client_licenses = [license_obj for license_obj in all_filtered_licenses if license_obj.client == client]

        if client_licenses:
            # Prepare email body
            email_body = prepare_email_body(client_licenses)

            # Send email
            send_mail(
                'License Expiry Notification',
                email_body,
                'from@example.com',
                [client.admin_poc.email],
                fail_silently=False
            )

            # Logging the email notification
            for license_obj in client_licenses:
                EmailLog.objects.create(
                    sent_time=today,
                    license_id=license_obj.id
                )

