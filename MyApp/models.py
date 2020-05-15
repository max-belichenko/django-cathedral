import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone


class ArticleAbout(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField('Active?')

    header = models.CharField('Header', max_length=200)
    text = models.TextField('Text')
    picture = models.ImageField('Picture', upload_to='uploads/')

    def __str__(self):
        return self.text
