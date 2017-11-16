from django.db import models

# Create your models here.

class Friend(models.Model):
    user1 = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='friends_1')
    user2 = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='friends_2')
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'friends'

    def __str__(self):
        return '{user1} - {user1}'.format(user1=user1,user2=user1)
