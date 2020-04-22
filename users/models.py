from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    LANDLORD = 1
    TENANT = 2

    ROLE_CHOICES =(
        (LANDLORD, 'Landlord'),
        (TENANT, 'Tenant'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    id_number = models.CharField(max_length=250,blank=True,null=True)
    phone = models.CharField(max_length=250,blank=True,null=True)

    REQUIRED_FIELDS = ["email", "role","id_number","phone"]
