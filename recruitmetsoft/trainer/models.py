from django.db import models

class Trainer(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    tech_stack = models.CharField(max_length=200)
    total_experience = models.DecimalField(max_digits=4, decimal_places=1)
    is_active = models.BooleanField(default=True)
    # example: 3.5 years

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.username
