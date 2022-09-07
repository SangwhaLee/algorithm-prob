from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return self.title