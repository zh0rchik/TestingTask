from rest_framework import viewsets, serializers
from shops.models import City, Street, Shop

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'city_name')


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('street_name',)

class CityStreetsSerializer(serializers.ModelSerializer):
    streets = StreetSerializer(many=True, read_only=True, source='street_set')

    class Meta:
        model = City
        fields = ('city_name', 'streets')

class ShopSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.city_name', read_only=True)
    street_name = serializers.CharField(source='street.street_name', read_only=True)

    class Meta:
        model = Shop
        fields = ('shop_name', 'city_name', 'street_name', 'city', 'street', 'home', 'open_time', 'close_time')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['city'] = representation.pop('city_name')
        representation['street'] = representation.pop('street_name')
        return representation

    def validate(self, data):
        if data['street'].city != data['city']:
            raise serializers.ValidationError("The street is not in the specified city.")
        return data

    def create(self, validated_data):
        return Shop.objects.create(**validated_data)