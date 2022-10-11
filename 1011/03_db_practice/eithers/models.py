from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    RED_TEAM = models.CharField(max_length = 100)
    BLUE_TEAM = models.CharField(max_length = 100)

    def __str__(self):
        return self.title


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.CharField(max_length=10)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.title


