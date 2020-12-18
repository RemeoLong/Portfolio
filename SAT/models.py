from django.db import models


class Test(models.Model):
    test = models.CharField(max_length=20)

    def __str__(self):
        return self.test


class Section(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
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

    def __str__(self):
        return self.choice_text

    def check_answer(self, choice):
        return self.choices_set.filter(id=choice.id, correct='Correct').exists()

    def get_answer(self):
        return self.choices_set.filter(correct='Correct')


class Answer(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    answer = models.CharField(blank=True, max_length=500, default='')
