from django.db import models
from django.contrib.auth.models import User

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agent_profile')
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    hire_date = models.DateField()

    def __str__(self):
        return self.user.username
