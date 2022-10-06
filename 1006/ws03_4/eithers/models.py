from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    RED_TEAM = models.CharField(max_length = 100)
    BLUE_TEAM = models.CharField(max_length = 100)

    def __str__(self):
        return self.title


class Comment(models.Model):
    TEAM_PICK = (
        ('RED TEAM','RED TEAM'),
        ('BLUE TEAM','BLUE TEAM'),
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.CharField(max_length=10, choices = TEAM_PICK, default='RED TEAM')
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.title


