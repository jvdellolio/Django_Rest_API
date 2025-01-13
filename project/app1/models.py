from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    about = models.TextField()
    linkedin = models.URLField()
    github = models.URLField()