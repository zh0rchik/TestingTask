from datetime import datetime

from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from shops.models import City, Shop
from shops.serializers import CitySerializer, CityStreetsSerializer, ShopSerializer


# Create your views here.

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetail(APIView):
    def get_object(self, pk):
        try:
            city = City.objects.get(pk=pk)
            return city
        except City.DoesNotExist:
            from django.http import Http400
            raise Http400

    def get(self, request, pk):
        city = self.get_object(pk)
        serializer = CityStreetsSerializer(city)
        return Response(serializer.data)


class ShopDetail(APIView):
    def get_queryset(self):
        city = self.request.query_params.get('city', None)
        street = self.request.query_params.get('street', None)
        is_open = self.request.query_params.get('open', None)
        shops = Shop.objects.all().prefetch_related('street', 'city')

        filter_params = {}

        if city:
            filter_params['city__city_name'] = city
        if street:
            filter_params['street__street_name'] = street

        if is_open is not None and is_open.isdigit():
            current_time = datetime.now().time()
            if int(is_open) == 1:
                shops = shops.filter(open_time__lte=current_time, close_time__gte=current_time)

            elif int(is_open) == 0:
                shops = shops.filter(~Q(open_time__lte=current_time, close_time__gte=current_time))

        return shops.filter(**filter_params)

    def get(self, request):
        shops = self.get_queryset()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data.get('id'))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)