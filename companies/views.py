from rest_framework import generics
from .models import Company
from .serializers import CompanySerializer, CompanyListAllSerializer
from utils.mixins import SerializerByMethodMixin


class CompanyView(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_map = {
        "GET": CompanyListAllSerializer,
        "POST": CompanySerializer
    }


class CompayDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_url_kwarg = "company_id"