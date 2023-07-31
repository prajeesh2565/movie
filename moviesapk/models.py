from django.db import models

# Create your models here.
class movies(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='images')
    desc=models.TextField()
    year=models.IntegerField()

    def __str__(self):
        return self.name