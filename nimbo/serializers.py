# serializers.py
from rest_framework import serializers
from .models import Machine


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['id', 'name', 'size_gb', 'operating_system', 'status']
