from django.db import models

# Create your models here.

class Friend(models.Model):
    user1 = models.TextField()
    user2 = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "friends"
        

