import datetime
from django.db import models
from django.utils import timezone
from .models import Question, Choice


class Passage(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    passage_text = models.CharField(max_length=10000)


class Explanation(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    explain = models.CharField(max_length=500)
