from django.db import models

class Institute(models.Model):
    institute_name = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    course_offered = models.CharField(max_length=100)
    tech_stack = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.institute_name
