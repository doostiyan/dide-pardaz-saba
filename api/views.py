from rest_framework import generics, filters
from django.db.models import F
from api.serializers import PhoneSerializer
from shop.models import Mobile


class MobileFilterView(generics.ListAPIView):
    serializer_class = PhoneSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['brand__name', 'brand__nationality', 'manufacture_country']

    def get_queryset(self):
        queryset = Mobile.objects.all()

        return queryset


class MatchingMobilesList(generics.ListAPIView):
    serializer_class = PhoneSerializer

    def get_queryset(self):
        return Mobile.objects.filter(brand__nationality=F('manufacture_country'))