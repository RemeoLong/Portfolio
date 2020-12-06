import datetime
from django.db import models
from django.utils import timezone


class Passage(models.Model):
    passage_text = models.CharField(max_length=10000)

    def __str__(self):
        return self.passage_text


class Explanation(models.Model):
    explain_text = models.CharField(max_length=500)

    def __str__(self):
        return self.explain_text


class Question(models.Model):
    passage = models.ForeignKey(Passage, on_delete=models.CASCADE)
    questions_text = models.CharField(max_length=400)

    def __str__(self):
        return self.questions_text


class Choice(models.Model):
    correct_choices = (
        ("Correct", "Correct"),
        ("Incorrect", "Incorrect"),
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    explain = models.ForeignKey(Explanation, on_delete=models.CASCADE, default="")
    choice_text = models.CharField(max_length=200)
    correct = models.CharField(max_length=10, choices=correct_choices, default='Incorrect')

    def __str__(self):
        return self.choice_text

    def check_answer(self, choice):
        return self.choices_set.filter(id=choice.id, is_answer=True).exists()

    def get_answer(self):
        return self.choices_set.filter(is_answer=True)

