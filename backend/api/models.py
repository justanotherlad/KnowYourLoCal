from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.TextField()


class Resource(models.Model):
    name = models.TextField()
    category = models.ForeignKey(to="Category", on_delete=models.SET_NULL, null=True)
    lat = models.DecimalField(max_digits=22, decimal_places=16)
    long = models.DecimalField(max_digits=22, decimal_places=16)
    phone = PhoneNumberField(blank=False, null=False)
