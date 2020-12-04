import datetime
from django.db import models
from django.utils import timezone


class Passage(models.Model):
    passage_text = models.CharField(max_length=10000)

    def __str__(self):
        return self.passage_text


class Question(models.Model):
    passage = models.ForeignKey(Passage, on_delete=models.CASCADE)
    questions_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.questions_text

    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

    def check_answer(self, choice):
        return self.choices_set.filter(id=choice.id, is_answer=True).exists()

    def get_answer(self):
        return self.choices_set.filter(is_answer=True)


class Explanation(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    explain = models.CharField(max_length=500)

    def __str__(self):
        return self.explain


