from django.db import models

# Create your models here.


class Book(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    year = models.IntegerField()

    def __str__(self):
        return self.name