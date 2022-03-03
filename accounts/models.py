from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import MaxLengthValidator, MinLengthValidator


class UserManager(BaseUserManager):
    def create_user(
        self, email, username, password=None, is_staff=False, is_admin=False,
        is_active=True, is_labour=False
    ):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user_obj = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj._labour = is_labour
        # user_obj.is_labour = is_labour

        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, username, password, is_labour=False):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, is_labour=False):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
            is_labour=is_labour
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=255, validators=[
        MaxLengthValidator(20),
        MinLengthValidator(3),
    ], unique=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    _labour = models.BooleanField(default=False)

    objects = UserManager()

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    # Email & Password are required by default.
    REQUIRED_FIELDS = ['username', ]

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_labour(self):
        "Is the user is a labour"
        return self._labour
