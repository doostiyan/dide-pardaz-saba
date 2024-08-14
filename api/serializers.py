from rest_framework import serializers
from shop.models import Brand, Mobile


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    brand_nationality = serializers.CharField(source='brand.nationality', read_only=True)
    class Meta:
        model = Mobile
        fields = '__all__'
