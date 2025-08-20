from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from lms.models import Course, Subscription
from users.models import User


@shared_task
def send_message_update(course_pk):
    course = Course.objects.get(pk=course_pk)
    subscriptions = Subscription.objects.filter(course=course.pk)
    subscribers = [subscription.user.email for subscription in subscriptions]

    send_mail(
        "Обновление курса",
        "Курс, на который Вы подписаны был обновлен.",
        EMAIL_HOST_USER,
        subscribers,
    )


@shared_task
def deactive_user():
    one_month_ago = timezone.now() - timezone.timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago, is_active=True)

    if inactive_users:
        for user in inactive_users:
            user.is_active = False
            user.save()
