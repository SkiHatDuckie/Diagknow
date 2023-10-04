from django.contrib import admin

# Register your models here.
from django.db import models
from .models import User, Symptom, Hospital, Illness

admin.register(User)
admin.register(Symptom)
admin.register(Hospital)
admin.register(Illness)