from django.db import models
from django.contrib.auth.models import User

from projects.models import Department

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    department = models.ManyToManyField(Department)