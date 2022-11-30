from rest_framework import generics
from .models import Sector
from .serializers import SectorSerializer


class SectorView(generics.ListCreateAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer


class SectorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    lookup_url_kwarg = "sector_id"