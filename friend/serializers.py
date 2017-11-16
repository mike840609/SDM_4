from rest_framework import serializers
from friend.models import Friend

class FriendSerializer(serializers.ModelSerializer):
    class Meta:

        model = Friend
        fields = '__all__'

        # fields = ('id', 'user1','user2','created' )

    def get_days_since_created(self, obj):
       return (now() - obj.created).days    
