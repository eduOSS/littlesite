from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    regi_date = models.DateTimeField('registration time')
    coins = models.IntegerField(default=0)
    log_num = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class Clock(models.Model):
    user = models.ForeignKey(User)
    clock_text = models.CharField(max_length=200)
    clock_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.clock_text
    def was_clocked_recently(self):
        return datetime.timedelta(days = 1) <= timezone.now() - self.clock_date 
