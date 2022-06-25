from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student

# Validators Function
def start_with_r(value):
    if value[0].lower()!= 'r':
        raise serializers.ValidationError('Name should be start with R')
    return value


class StudentSerializer(serializers.Serializer):
    roll = serializers.IntegerField()
    name = serializers.CharField(max_length=100, validators = [start_with_r])
    city = serializers.CharField(max_length=100)

    #  Field Level Validation

    def validate_roll(self, value):
        if value >=200:
            raise serializers.ValidationError('Seat Full')
        return value

    # Object Level Validation

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'chetan' and ct.lower() != 'surat':
            raise serializers.ValidationError('City must be Surat')
        return data



    def create(self, validated_data):
        return Student.objects.create(**validated_data)   # Data Insert into Database
    
    def update(self, instance, validate_data):      # Data Update 
        print(instance.name)
        instance.name = validate_data.get('name', instance.name)
        print(instance.name)
        instance.roll = validate_data.get('roll', instance.roll)
        print(instance.roll)
        instance.city = validate_data.get('city', instance.city)
        print(instance.city)
        instance.save()
        return instance
