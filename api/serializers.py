from rest_framework import serializers
from .models import Profile
from .models import Promise
from .models import Progress

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'firstname', 'lastname', 'nickname', 'about')

class PromiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promise
        fields = ('id', 'charity_name', 'duration', 'target_heartbeats')

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ('id', 'start_date', 'current_heartbeats')
