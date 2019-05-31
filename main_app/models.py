from django.db import models

# Create your models here.
class Chat(models.Model):
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name
