from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Quiz(models.Model):
    name=models.CharField(max_length=50)
    time_duration=models.PositiveIntegerField()

class Question(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)
    question_text=models.CharField(null=True,max_length=250)
    question_image=models.ImageField(blank=True,null=True,upload_to="uploads")

class Option(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,null=True)
    option_text=models.CharField(max_length=100)
    is_correct=models.BooleanField(default=False)

class StudentAttempt(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    score=models.PositiveIntegerField(default=0)
    attempted_on=models.DateTimeField(auto_now_add=True)