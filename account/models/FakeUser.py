from django.db import models

class FakeUser(models.Model):
    owner = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='holders')
    name = models.CharField(max_length=16)

    last_modify = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'fake_users'

    def __str__(self):
        return '{name} ({owner})'.format(owner=self.owner, name=self.name)
