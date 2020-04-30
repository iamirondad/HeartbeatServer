from django.db import models

# Create your models here.
class Profile(models.Model):
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    nickname = models.CharField(max_length=256)
    about = models.TextField()

class Promise(models.Model):
    charity_name = models.CharField(max_length=256)
    duration = models.DurationField(None)
    target_heartbeats = models.IntegerField(default=1000000)

class Progress(models.Model):
    start_date = models.DateField(None)
    current_heartbeats = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "Progressions"
