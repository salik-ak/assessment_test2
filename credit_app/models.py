from django.db import models
from django.contrib.auth.models import User

# Model to store questions
class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=50)
    option_b = models.CharField(max_length=50)
    option_c = models.CharField(max_length=50)
    option_d = models.CharField(max_length=50)
    score_a = models.IntegerField(default=0)
    score_b = models.IntegerField(default=0)
    score_c = models.IntegerField(default=0)
    score_d = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text

# Model to store user responses
class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=1)
    timestamp = models.DateTimeField(auto_now_add=True)

