from rest_framework import serializers
from .models import Company
from sectors.serializers import SectorSerializer
from sectors.models import Sector
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.exceptions import NotFound
from django.core.exceptions import ValidationError


class CompanyListAllSerializer(serializers.ModelSerializer):
    sector = SectorSerializer(read_only=True)

    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "opening_hours",
            "description",
            "sector",
        ]


class CompanySerializer(serializers.ModelSerializer):
    # sector = SectorSerializer(read_only=True)
    sector_id = serializers.CharField()

    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "opening_hours",
            "description",
            # "sector",
            "sector_id",
        ]

    def create(self, validated_data):
        body = {**validated_data}

        sector_data = body.pop("sector_id")

        try:
            sector = get_object_or_404(Sector, pk=sector_data)
        except ValidationError:
            raise NotFound("Sector not found!")

        company = Company.objects.create(
            name=body.pop("name"),
            opening_hours=body.pop("opening_hours"),
            description=body.pop("description"),
            sector_id=sector.id,
        )

        return company

    def update(self, instance, validated_data):
        body = {**validated_data}

        name_data = body.pop("name", None)
        opening_hours_data=body.pop("opening_hours", None)
        description_data=body.pop("description", None)
        sector_id_data=body.pop("sector_id", None)

        if name_data is not None:
            instance.name = name_data
        
        if opening_hours_data is not None:
            instance.opening_hours = opening_hours_data
        
        if description_data is not None:
            instance.description = description_data
        
        if sector_id_data is not None:
            try:
                sector = get_object_or_404(Sector, pk=sector_id_data)
            except ValidationError:
                raise NotFound("Sector not found!")
            
            instance.sector_id = sector.id
        
        instance.save()

        return instance