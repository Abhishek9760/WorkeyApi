from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator

User = get_user_model()

# Create your models here.


class Labour(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    age = models.IntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(18),
    ])
    expertise = models.CharField(max_length=255)
    experience = models.IntegerField()
    mobile = models.CharField(null=True, blank=True, max_length=10)
    address = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user.username) + "-L"
