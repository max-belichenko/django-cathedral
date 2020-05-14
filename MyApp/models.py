import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class ArticleAbout(models.Model):
    author = models.CharField('Author', max_length=200)
    create_date = models.DateTimeField('Creation date', auto_now=True, auto_now_add=False)
    active = models.BooleanField('Active?')

    header = models.CharField('Header', max_length=200)
    text = models.TextField('Text')
    picture = models.ImageField('Picture', upload_to='uploads/')

    def __str__(self):
        return self.text
