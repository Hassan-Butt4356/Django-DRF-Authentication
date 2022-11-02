from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, dob, security_question, security_answer,
                   business_name, business_type, dba, monthly_volume, password=None, *args, **kwargs):

        if not username:
            raise ValueError('Username is Required')
        if not first_name:
            raise ValueError('First Name is Required')
        if not last_name:
            raise ValueError('Last Name is Required')
        if not email:
            raise ValueError('Email is Required')
        if not dob:
            raise ValueError('Date of Birth is Required')
        if not security_question:
            raise ValueError('Security Question is Required')
        if not security_answer:
            raise ValueError('Security Answer is Required')
        if not business_name:
            raise ValueError('business_name  is Required')
        if not business_type:
            raise ValueError('business type  is Required')
        if not dba:
            raise ValueError('dba  is Required')
        if not monthly_volume:
            raise ValueError('monthly_volume  is Required')

        user = self.model(first_name=first_name, last_name=last_name, email=self.normalize_email(email),
                          username=username, dob=dob, security_question=security_question,
                          security_answer=security_answer, business_name=business_name, business_type=business_type,
                          dba=dba, monthly_volume=monthly_volume)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, dob, security_question, security_answer,
                         business_name, business_type, dba, monthly_volume, password, *args, **kwargs):

        user = self.creat_user(first_name=first_name, last_name=last_name, email=self.normalize_email(email),
                               username=username, dob=dob, security_question=security_question,
                               security_answer=security_answer, business_name=business_name,
                               business_type=business_type,
                               dba=dba, monthly_volume=monthly_volume, password=password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    email = models.EmailField(max_length=155)
    dob = models.DateTimeField(max_length=155)
    username = models.CharField(max_length=155,unique=True)

    security_question = models.CharField(max_length=255)
    security_answer = models.CharField(max_length=255)
    business_name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=255)

    dba = models.CharField(max_length=55)
    monthly_volume = models.CharField(max_length=155)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'dob', 'security_question', 'security_answer',
                       'business_name', 'business_type', 'dba', 'monthly_volume']
    objects = UserManager()

    def __unicode__(self):
        return self.username

class Item(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Song(models.Model):
    name=models.CharField(max_length=155)
    singers=models.ManyToManyField(User)

    def __str__(self):
        return self.name

    @property
    def get_all_singers(self):
        return self.singers.all()
