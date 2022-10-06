from __future__ import absolute_import
import os, datetime
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings')

app.conf.beat_schedule = {
    'add-coin-market-checker': {
        'task': 'home.tasks.bulk_added_coin_market',
        'schedule': crontab(minute='*/1'),                # every 1 minute
    },
    'update-coin-market-checker': {
        'task': 'home.tasks.bulk_update_coin_market',
        'schedule': datetime.timedelta(seconds=30),                # every 30 seconds
    }
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)