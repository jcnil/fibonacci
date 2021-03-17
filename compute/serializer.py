from rest_framework import serializers
from . models import *


class ComputeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compute
        fields = ['number', 'serie_fibonacci']
