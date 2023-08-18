from django.db import models

class Settings(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Name of the setting
    value = models.CharField(max_length=1000)  # Value of the setting

    def __str__(self):
        return self.name
