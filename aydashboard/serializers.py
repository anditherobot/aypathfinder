from rest_framework import serializers
from ayregistration.models import * 


class RequestorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationCheckList
        fields = '__all__'

