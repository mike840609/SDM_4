from django.db import models


class Friend(models.Model):
    user1 = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='friends_1')
    user2 = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='friends_2')
    last_modify = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'friends'

    def __str__(self):
        return '{user1} - {user2}'.format(user1=self.user1,user2=self.user2)
