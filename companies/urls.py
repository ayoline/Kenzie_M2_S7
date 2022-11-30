from django.urls import path
from .views import CompanyView, CompayDetailView

urlpatterns = [
    path("companies/", CompanyView.as_view()),
    path("companies/<company_id>/",CompayDetailView.as_view()),
]
