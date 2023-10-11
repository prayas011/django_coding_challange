from typing import List, Any

from django.core.mail import send_mail
from django.template import Template
from django.template.loader import get_template


DEFAULT_FROM_EMAIL = 'noreply@email.com'


class EmailNotification:
    subject = None  
    from_email = DEFAULT_FROM_EMAIL  
    template_path = None 

    @classmethod
    def load_template(cls) -> Template:
        return get_template(cls.template_path)

    @classmethod
    def send_notification(cls, recipients: List[str], context: Any):
        template = cls.load_template()
        message_body = template.render(context=context)
        send_mail(cls.subject, message_body, cls.from_email, recipients, fail_silently=False)
