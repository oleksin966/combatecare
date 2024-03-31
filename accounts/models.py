from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.contrib.auth.models import Group, Permission
from .permissions import volunteer_permissions


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        #username = self.normalize_email(username)
        #encrypted_password = make_password(password)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=60, null=True, blank=True)
    info = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='user_photo/%Y/%m/%d/', null=True, blank=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='users')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Учасник'
        verbose_name_plural = 'Всі Учасники'

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.username

class Volunteer(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True, related_name='volunteer')

    class Meta:
        verbose_name = 'Волонтер'
        verbose_name_plural = 'Волонтери'

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Volunteer, self).save(*args, **kwargs)
        volunteer_group, created = Group.objects.get_or_create(name='Volunteer')
        if created:
            volunteer_group.permissions.set(volunteer_permissions)
        self.user.groups.add(volunteer_group)
        
class Military(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True,related_name='military')
    military_unit = models.CharField(max_length=255)
    military_rank = models.CharField(max_length=40, blank=True, null=True)
    class Meta:
        verbose_name = 'Військовий'
        verbose_name_plural = 'Військові'



class Deliveryman(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True,related_name='deliveryman')
    STATUS_CHOICES = [
        ('В дорозі', 'В дорозі'),
        ('Вільний', 'Вільний'),
        ('Недоступний', 'Недоступний'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, default='Вільний', max_length=20)

    class Meta:
        verbose_name = 'Доставщик'
        verbose_name_plural = 'Доставщики'

    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    volunteer = models.OneToOneField(Volunteer, on_delete=models.CASCADE, blank=True, null=True)
    military = models.OneToOneField(Military, on_delete=models.CASCADE, blank=True, null=True)
    deliveryman = models.OneToOneField(Deliveryman, on_delete=models.CASCADE, blank=True, null=True)
    avatar = models.ImageField(upload_to='update_user_photo/%Y/%m/%d/', default='/static/account/img/noavatar.png', blank=True, null=True)
    # add fields from Volunteer, Military, and Deliveryman models here


