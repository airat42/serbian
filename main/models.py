from django.db import models

class Dictionary(models.Model):
    russian = models.CharField(max_length=255)
    serbian = models.CharField(max_length=255)
    def __str__(self):
        return self.russian
