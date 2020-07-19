from django.db import models
from django.contrib.auth.models import User


class Allergy(models.Model):
    ALLERGISE_CHOICES = (
        ('Shellfish', 'Shellfish'),
        ('Milk', 'Milk'),
        ('Eggs', 'Eggs'),
        ('Soy', 'Soy'),
        ('Wheat', 'Wheat'),
        ('Fish', 'Fish'),
        ('Peanuts', 'Peanuts'),
        ('Walnuts', 'Walnuts'),
        ('Citrus', 'Citrus'),
        ('Strawberry', 'Strawberry'),
    )
    user_id          = models.ForeignKey(User, on_delete=models.CASCADE)  # stores 1:n relationship user:allergy
    dateCreated      = models.DateField(auto_now_add=True)
    dateCompleted    = models.DateField(null=True, blank=True)
    New_Allergy      = models.CharField(max_length=70, choices = ALLERGISE_CHOICES)
    description      = models.TextField(default=False)
    Life_threatening = models.BooleanField(default=False)


    def __str__(self):
        return self.New_Allergy



class Hospitalization(models.Model):
    user_id          = models.ForeignKey(User, on_delete=models.CASCADE)
    dateCreated      = models.DateField(auto_now_add=True)
    dateCompleted    = models.DateField(null=True, blank=True)
    Name_of_hospital = models.CharField(max_length=100)
    description      = models.TextField(default=False)


    def __str__(self):
        return self.Name_of_hospital


