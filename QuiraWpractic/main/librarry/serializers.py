from rest_framework import serializers
from .models import Library

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'number']
        model = Library

    def validate_number(self, value):
        if value < 5:
            raise serializers.ValidationError('Number must be 5 or greater.')
        return value
