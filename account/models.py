from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_patient = models.BooleanField('Is patient', default=False)
    is_doctor = models.BooleanField('Is doctor', default=False)