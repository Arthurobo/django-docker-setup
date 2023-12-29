from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def confirm_celery_running():
    context =  {}
    email_msg = EmailMessage(
        "New Review",
        "HAHA TODAY OOO", 
        ["test@test.com",], # From Email
        ["test@test.com",], # To Email
        reply_to=[settings.DEFAULT_FROM_EMAIL,]
    )
    email_msg.send(fail_silently=False)
    return email_msg