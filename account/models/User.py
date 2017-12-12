import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, username, uid, **kwargs):
        if not email:
            raise ValueError('The given email must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, name=username, user_fb_id=uid, **kwargs)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, name, user_fb_id, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, user_fb_id=user_fb_id, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)

    user_fb_id = models.CharField(max_length=64)

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=16)

    created = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'user_fb_id']

    class Meta:
        db_table = 'users'

    def __str__(self):
        return '{name} ({email})'.format(name=self.name, email=self.email)

    def get_long_name(self):
        return self.name

    def get_short_name(self):
        return self.name
