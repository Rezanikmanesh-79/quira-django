from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    minimum_price=serializers.IntegerField()
    maximum_price=serializers.IntegerField()
    cuntry=serializers.CharField(max_length=100)

    def validate(self,data):
        if data.get('minimum_prce',0)> data.get('maximum_price',0):
            erroe='Maximum shuld be greater than minimum'
            raise serializers.ValidationErro(erroe)
        return data
    
    def create(self,validated_data):
        book=book.objects.create(**validated_data)
        return book
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get(
            'name',instance.name
        )
        instance.minimum_prce=validated_data.get(
            'minimum_prce',instance.minimum_prce
        )
        instance.maximum_price=validated_data.get(
            'maximum_price',instance.maximum_price
        )
        instance.cuntry=validated_data.get(
            'cuntry',instance.cuntry
        )

        instance.save()
        return instance