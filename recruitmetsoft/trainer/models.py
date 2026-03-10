from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    tech_stack = models.CharField(max_length=200)
    total_experience = models.DecimalField(max_digits=4, decimal_places=1)  
    # example: 3.5 years

    def __str__(self):
        return self.name