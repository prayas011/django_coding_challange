from django.db import models


class LicenseManager(models.Manager):
    def expiring_in_4_months(self):
        # logic to get licenses expiring in 4 months
        return self.filter(expiration_date__range=[timezone.now(), timezone.now() + timedelta(days=120)])

    def expiring_within_a_month_and_monday(self):
        if timezone.now().weekday() == 0:  # Check if today is Monday
            return self.filter(expiration_date__lte=timezone.now() + timedelta(days=30))

    def expiring_within_a_week(self):
        return self.filter(expiration_date__lte=timezone.now() + timedelta(days=7))

class License(models.Model):
    # your fields here
    ...
    objects = LicenseManager()

class EmailLog(models.Model):
    sent_at = models.DateTimeField(auto_now_add=True)
    license_id = models.ForeignKey(License, on_delete=models.CASCADE)

