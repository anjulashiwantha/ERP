from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class create(models.Model):
    issue = (
        ('cleared', 'cleared'),
        ('pending', 'pending'),
        ('flagger', 'flagger'),
    )

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    NIC_Number = models.CharField(max_length=200, null=True)
    Name = models.CharField(max_length=200, null=True)
    Issues = models.CharField(max_length=200, null=True, choices=issue)
    Remark = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)



    def __str__(self):
        return self.Name

class UserCreated(models.Model):
    user = (
        ('admin', 'admin'),
        ('Data_Entry', 'Data_Entry'),
    )

    user_name = models.CharField(max_length=200, null=True)
    nic_number = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    password1 = models.CharField(max_length=100, null=True)
    password2 = models.CharField(max_length=100, null=True)
    User_Roles = models.CharField(max_length=200, null=True, choices=user)

    def __str__(self):
        return self.user_name
