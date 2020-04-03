from rest_framework import serializers
from .models import Profile
from .models import Promise
from .models import Progress

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'realname', 'nickname', 'about')

class PromiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promise
        fields = ('id', 'start_date', 'duration', 'target_heartbeats')

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ('id', 'current_heartbeats')
