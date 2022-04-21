from dataclasses import field
from pandas import Series
from rest_framework import serializers
from api.models import Company, Vacancy

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(default="", max_length=200)
    city = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=100)

    def create(self, validated_data):
        company = Company.objects.create(
            name=validated_data.get('name'),
            description=validated_data.get('description'),
            city=validated_data.get('city'),
            address=validated_data.get('address')
            )
        return company
    
    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.city = validated_data['city']
        instance.address = validated_data['address']
        instance.save()
        return instance

class VacancySerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company')