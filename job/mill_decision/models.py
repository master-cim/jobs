from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime
import pytz


class Posting(models.Model):
    start = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(default=datetime.timedelta(days=7))
    text = models.TextField()
    client_filter = models.CharField(max_length=50)

    @property
    def finish(self):
        return self.start + self.duration
    
    def __str__(self):
        return self.client_filter


class Client(models.Model):    
    phone = models.PositiveIntegerField(
        validators=[MinValueValidator(70000000000),
                    MaxValueValidator(79999999999)])
    mobile_code = models.CharField(max_length=3, blank=False)
    tag = models.CharField(max_length=50)
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    timezone = models.CharField(max_length=32, choices=TIMEZONES,
                                default='Europe/Moscow')


class Message(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    sending_status = models.CharField(max_length=250)
    id_posting = models.ForeignKey(
        Posting,
        on_delete=models.CASCADE
    )
    id_client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )
