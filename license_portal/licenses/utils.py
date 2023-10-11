from django.core.mail import send_mail

def send_license_notification_email(license):
    subject = 'License Expiry Notification'
    message = f'''
    License id: {license.id}
    License type: {license.license_type}
    Name of the package: {license.package_name}
    Expiration date: {license.expiration_date}
    POC information: {license.poc_information}
    '''
    send_mail(subject, message, 'from_email@example.com', ['to_email@example.com'])
