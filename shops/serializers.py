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


# Serializer that returns streets of a city
class CityStreetsSerializer(serializers.ModelSerializer):
    streets = StreetSerializer(many=True, read_only=True, source='street_set')

    class Meta:
        model = City
        fields = ('city_name', 'streets')


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('shop_name', 'street', 'city', 'home', 'open_time', 'close_time')