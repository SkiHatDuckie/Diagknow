from decimal import MAX_EMAX
from sys import maxsize
from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.
from django.views.decorators.http import condition
from catalog import models


class Illness(models.Model):
    symptom = models.ForeignKey(models.Symptom, on_delete=models.CASCADE)


class Symptom(models.Model):
    victims = models.ManyToManyField(models.User, through="symptoms")
    diseases = models.ForeignKey(models.Illness, on_delete=models.CASCADE, to_field=models.User, through_fields="symptom")


class Hospital(models.Model):
    location = models.TextField(max_length=100)
    num_users = models.IntegerField()
    phone = models.CharField(max_length=10)



class User(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author is a string rather than an object because it hasn't been declared yet in the file
    userName = models.CharField(max_length=20)
    password = models.TextField(max_length=30)
    phone = models.TextField(max_length=30, help_text='Enter your phone number')
    email = models.ForeignKey('email', unique=True,
                             help_text='Your email goes here.')
    hospital = models.ForeignKey(Hospital)
    condition = models.CharField(max_length=MAX_EMAX)

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    symptoms = models.ManyToManyField(Symptom, through="condition", through_fields=("victims"), help_text='Your symptoms appear here.')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])
    
    def getCondition(self):
        return condition

    def getSymptoms(self):
        return self.symptoms.split(' ,', self.symptoms)

  