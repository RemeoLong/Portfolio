from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Test(models.Model):
    test = models.CharField(max_length=20)

    def __str__(self):
        return self.test


class Section(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, default="")
    section = models.CharField(max_length=30)

    def __str__(self):
        return self.section


class Passage(models.Model):
    passage_text = models.CharField(max_length=10000)

    def __str__(self):
        return self.passage_text


class Explanation(models.Model):
    explain_text = models.CharField(max_length=500)

    def __str__(self):
        return self.explain_text


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, default="")
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
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

    class Meta:
        ordering = ('question', 'choice_text', 'correct')

    def __str__(self):
        return self.choice_text

    def check_answer(self, choice):
        return self.choices_set.filter(id=choice.id, correct='Correct').exists()

    def get_answer(self):
        return self.choices_set.filter(correct='Correct')


class Answer(models.Model):
    UserID = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default="")
    answer = models.CharField(blank=True, max_length=500, default='')

    class Meta:
        ordering = ('UserID', 'answer')


class TotalScore(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, default='')
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ('User', 'test', 'section', 'score')

    @receiver(post_save, sender=User)
    def create_user_totalscore(sender, instance, created, **kwargs):
        if created:
            TotalScore.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_totalscore(sender, instance, **kwargs):
        instance.total.save()

