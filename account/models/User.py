import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from itertools import chain

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **kwargs):
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        return self._create_user(email, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=16)

    created = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = 'users'

    def __str__(self):
        return '{name} ({email})'.format(name=self.name, email=self.email)

    def get_long_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    @property
    def friends(self):
        friend_list = list(
            chain(
                    self.friends_1.all(),
                    self.friends_2.all()
                )
            )

        friends = []
        
        
        for friend in friend_list:
            # print ("================")
            # print (friend.user1.email)
            # print (friend.user2.email)
            
            friends.append({
                    'name': friend.user2.name if friend.user1.email == self.email else friend.user1.name,
                    'email': friend.user2.email if friend.user1.email == self.email else friend.user1.email,
                    'created': friend.created,
                    'last_modify':friend.last_modify
                })

        return friends
