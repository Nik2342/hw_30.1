import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.conf.result_backend = settings.CELERY_RESULT_BACKEND
app.conf.timezone = settings.TIME_ZONE

# Планировщик Celery Beat
app.conf.beat_schedule = {
    'check_inactive_users': {
        'task': 'users.tasks.check_inactive_users',
        'schedule': crontab(hour=0, minute=0),  # Ежедневно в полночь
    },
}

app.autodiscover_tasks()