from django.db import models

# Create your models here.

from decimal import MAX_EMAX
from sys import maxsize
from django.db import models as Models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

# Create your models here.
from django.views.decorators.http import condition
from datetime import datetime


class Symptom(Models.Model):
    name = Models.CharField(max_length=100)
    diseases = Models.ForeignKey(Models.Illness, on_delete=Models.CASCADE, to_field=Models.User,
                                 through_fields="symptom")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.

class Illness(Models.Model):
    symptoms = []
    def addSymptom(self, symptomName):
        symptom = Models.ForeignKey(Models.Symptom, on_delete=Models.CASCADE, through_fields="symptom", verbose_name=symptomName)
        self.symptoms.append(symptom)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.

class Hospital(Models.Model):
    location = Models.TextField(max_length=100)
    users = {
        "name": [],
        "age": [],
        "ID": [],
        "registration_date": [],
        "phone": [],
        "email": []
    }
    num_users = len(users["name"])
    def registerPatient(self, ID, name, phone, email, birthday):
        [day, month, year] = birthday.split(" ")
        if not (ID in self.users["name"]):
            self.users["name"].append(name)
            self.users["ID"].append(len(self.users["name"]))
            self.users["age"].append(datetime.today().year - year)
            self.users["registration_date"].append(datetime.today().strftime('%Y-%m-%d'))
            self.users["phone"].append(phone)
            self.users["email"].append(email)


    def assignDoctor(self, user): # inputs a User object, consists of name, ID, contact info, and perceived diagnosis
        return 0
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.

class Doctor(Models.Model):
    title = Models.CharField(max_length=100)
    specialty = Models.TextField(max_length=100)
    patients = []
    

class Pediatrician(Models.Model):
    patients = Models.ObjectField(max_length=10)
    meds = Models.StringField(max_length=10)
    prescriptions = {"medicines": [], "times": [], "vaccines": []}
    def getPatients(self):
        return self.patients

    def getMeds(self):
        return self.meds

    def getTime(self, med):
        times = self.prescriptions.get("times")
        return times[self.prescriptions.get("medicines").index(med)]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.


class User(Models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author is a string rather than an object because it hasn't been declared yet in the file
    userName = Models.CharField(max_length=20)
    password = Models.TextField(max_length=30)
    phone = Models.TextField(max_length=30, help_text='Enter your phone number')
    email = Models.ForeignKey('email', unique=True,
                              help_text='Your email goes here.')
    hospital = Models.ForeignKey(Hospital)
    condition = Models.CharField(max_length=MAX_EMAX)

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    symptoms = Models.ManyToManyField(Symptom, through="condition", through_fields="victims",
                                      help_text='Your symptoms appear here.')

    def getCondition(self):
        return self.condition

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
