from django.db import models

from decimal import MAX_EMAX
from sys import maxsize
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

# Create your models here.
from django.views.decorators.http import condition
from datetime import datetime
import numpy as np
from django.utils.text import slugify


class Hospital(models.Model):
    location = models.TextField(max_length=100)
    users = {
        "name": [],
        "age": [],
        "ID": [],
        "registration_date": [],
        "phone": [],
        "email": []
    }
    num_users = len(users["name"])


    class Meta:
        verbose_name = "Hospital"
        verbose_name_plural = "Hospitals"

    def registerPatient(self, ID, name, phone, email, birthday):
        [day, month, year] = birthday.split(" ")
        if not (ID in self.users["name"]):
            self.users["name"].append(name)
            self.users["ID"].append(len(self.users["name"]))
            self.users["age"].append(datetime.today().year - year)
            self.users["registration_date"].append(datetime.today().strftime('%Y-%m-%d'))
            self.users["phone"].append(phone)
            self.users["email"].append(email)
        user = User

    def assignDoctor(self, user): # inputs a User object, consists of name, ID, contact info, and perceived diagnosis
        return 0

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.


class Doctor(models.Model):
    title = models.CharField(max_length=100)
    options = {
        1: "cardiology",
        2: "dermatology",
        3: "endocrinology",
        4: "emergency meds",
        5: "family meds",
        6: "internal medicine",
        7: "neurology",
        8: "nuclear meds",
        9: "obstetrics",
        10: "ophthalmology"
    }
    # TODO: Add a callable validation check to see if speciatly falls into one of the `options`.
    specialty = models.BooleanField(verbose_name="specialty", primary_key=True)
    patients = []
    meds = models.CharField(max_length=10)
    prescriptions = {"medicines": [], "times": [], "vaccines": []}


    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def getType(self):
        type=""
        arr = {
            "age": [],
            "specialty": [],
            "patients_cap": 0,
            "hours": 0
        }
        return type

    def getPatients(self):
        return self.patients

    def getMeds(self):
        return self.meds

    def getTime(self, med):
        times = self.prescriptions.get("times")
        return times[self.prescriptions.get("medicines").index(med)]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.


class Pediatrician(Doctor):
    age_limit = models.IntegerField(verbose_name="age limit")


class Illness(models.Model):
    symptoms = []


    class Meta: pass
        # app_label = "Illness"

    def addSymptom(self, symptomName):
        symptom = models.ForeignKey(models.Symptom, on_delete=models.CASCADE,
                                    through_fields="symptom", verbose_name=symptomName)
        self.symptoms.append(symptom)

    def compareSigns(self, img):
        filter = [[1,0,1],[0,1,0],[1,0,1]]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.


class Symptom(models.Model):
    name = models.CharField(max_length=100)
    diseases = models.ManyToManyField(Illness, related_name="diseases")
    images = models.ForeignKey(Illness, related_name="images", on_delete=models.CASCADE)
    disease_effect_time = models.ManyToManyField(Illness, related_name="disease_effect_time")


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.


class User(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author is a string rather than an object because it hasn't been declared yet in the file
    username = models.CharField(max_length=20)
    password = models.TextField(max_length=30)
    phone = models.TextField(max_length=30, help_text='Enter your phone number')
    # TODO: The following line causes an error.
    # email = models.ForeignKey('email', on_delete=models.CASCADE, unique=True,
    #                           help_text='Your email goes here.')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    condition = models.CharField(max_length=MAX_EMAX)

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    # TODO: The following line causes an error.
    # symptoms = models.ManyToManyField(Symptom, through="condition", through_fields="victims",
    #                                   help_text='Your symptoms appear here.')
    doctor = models.ForeignKey(Doctor, unique=False, on_delete=models.CASCADE,
                               help_text='Medical doctor')


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def getCondition(self):
        return condition

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.

