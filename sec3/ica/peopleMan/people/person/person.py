import uuid
from django.db import models
from django.db.models import (
    UUIDField,
    CharField,
    IntegerField,
    BooleanField,
    DateTimeField,
    ImageField
)
from django_countries.fields import CountryField

# Create your models here.
class Person (models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fname = models.CharField(max_length=30, blank=False)
    lname = models.CharField(max_length=30)
    country = CountryField()

    def __str__ (self):
        return self.fname

class Meta:
    model = Person
    ordering = ('fname',)