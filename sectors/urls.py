from django.urls import path
from .views import SectorView, SectorDetailView

urlpatterns = [
    path("sectors/", SectorView.as_view()),
    path("sectors/<sector_id>/", SectorDetailView.as_view()),
]
