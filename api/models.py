from django.db import models

# Create your models here.
class Profile(models.Model):
    realname = models.CharField(max_length=256)
    nickname = models.CharField(max_length=256)
    about = models.TextField()

    def _str_(self):
        return self.nickname

class Promise(models.Model):
    start_date = models.DateField(None)
    duration = models.DurationField(None)
    target_heartbeats = models.IntegerField(default=1000000)

class Progress(models.Model):
    current_heartbeats = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "Progressions"
