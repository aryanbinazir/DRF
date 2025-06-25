from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    score = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])

    def __str__(self):
        return self.name

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.title[:20]}'

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uanswers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='qanswers')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.question.title[:20]}'




