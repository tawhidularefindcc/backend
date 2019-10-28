from rest_framework import serializers, exceptions
from .models import Profiles
import django.contrib.auth.password_validation as validators

class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ('creating_profile_for', 'firstname', 'lastname', 'gender', 'contact', 'email', 'password', 'confirm')

        def validate(self, attrs):
            if attrs[Profiles.password] != attrs[Profiles.confirm]:
                raise serializers.ValidationError({'password mismathced'})
            try:
                validators.validate_password(attrs[Profiles.password])
            except exceptions.ValidationError as e:
                raise serializers.ValidationError({'password is not valid'})
            return attrs




