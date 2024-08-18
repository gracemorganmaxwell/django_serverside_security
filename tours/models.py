from django.db import models
from django.contrib.auth.models import User

class Tour(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    managed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tours')

    def __str__(self):
        return self.name
