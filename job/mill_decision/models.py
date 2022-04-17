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
        return self.text


class Client(models.Model):
    phone = models.PositiveIntegerField(
        validators=[MinValueValidator(70000000000),
                    MaxValueValidator(79999999999)])
    mobile_code = models.CharField(max_length=3, blank=False)
    tag = models.CharField(max_length=50)
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    timezone = models.CharField(max_length=32, choices=TIMEZONES,
                                default='Europe/Moscow')

    def __str__(self):
        return f'{self.phone}'


class Message(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    sending_status = models.CharField(max_length=250)
    client = models.ForeignKey(
        Client,
        null=False,
        on_delete=models.CASCADE,
        related_name='message'
    )
    posting = models.ForeignKey(
        Posting,
        null=False,
        on_delete=models.CASCADE,
        related_name='message'
    )

    def __str__(self):
        return(f'{self.pub_date} {self.client}'
               f'{self.posting} {self.sending_status}')
