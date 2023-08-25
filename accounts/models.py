from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime

# import uuid


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email must be given')
        kwargs.setdefault('is_superuser', False)
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', False)

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email must be given')
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', True)

        superuser = self.model(email=self.normalize_email(email), **kwargs)
        superuser.set_password(password)
        superuser.save(using=self._db)
        return superuser


class Users(AbstractBaseUser, PermissionsMixin):
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    fullname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True, db_index=True)
    password = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='profile/')
    reg_date = models.DateTimeField(default=datetime.now, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__ (self):
        return str(self.email)
    
    def has_perms(self, perm, obj=None):
        return str(self.is_superuser)
    
    def get_full_name(self):
        return str(self.email)
    
    def has_module_perms(self, app_label):
        return True