from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()


class Comment(models.Model):
    
    RATE_CHOICES = (
        ('1', 'Very Dissatisfied'),
        ('2', 'Dissatisfied'),
        ('3', 'Good'),
        ('4', 'Satisfied'),
        ('5', 'Very Satisfied'),
    )
    
    name = models.CharField("name", max_length=50, blank=True, default='Anonymus', null=True)
    comment = models.TextField("comment", max_length=500, null=True)
    date = models.DateTimeField("date", auto_now_add=True, null=True)
    rate = models.CharField("rate", max_length=1, choices=RATE_CHOICES)
    
    def __str__(self):
        return self.name
    
class Client(models.Model):
    
    name = models.CharField("name", max_length=50, default='Anonymus', null=True)
    phone_number = PhoneNumberField("phone_number", null=True)
    email = models.EmailField("email", max_length=240, blank=True, null=True)
    message = models.TextField("message", max_length=500, null=True)
    date = models.DateTimeField("date", auto_now_add=True, null=True)

    def __str__(self):
        return self.name