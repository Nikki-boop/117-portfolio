from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='static/img/')
    repository = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f"{self.name} - {self.year}"
   

# Create your models here.
