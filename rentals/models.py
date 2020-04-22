from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
RENTAL_CHOICES =(
    ('R', 'Residential'),
    ('C','Commercial')
)


class Estate(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('estate_detail', args=[str(self.id)])

class Rental(models.Model):
    estate =  models.ForeignKey(
        Estate,
        on_delete=models.CASCADE,
        )

    manager = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    category = models.CharField(choices=RENTAL_CHOICES, max_length=1)

    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    rent = models.BigIntegerField(null=True,blank=True)
    is_occupied = models.BooleanField(default = False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " in " + self.estate.title

    def get_absolute_url(self):
        return reverse('rental_detail', args=[str(self.id)])
