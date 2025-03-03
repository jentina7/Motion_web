from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"home", HomeViewSet, basename="home-list"),

urlpatterns = [
    path("", include(router.urls)),

    # path('home/', HomeViewSet),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', UniversityListAPIView.as_view(), name='country_detail'),
    path('university/<int:pk>/', UniversityDetailListAPIView.as_view(), name='university_detail'),
    path('consultation_for_home/', ConsultationForHomeCreateAPIView.as_view(), name='consultation_for_home'),
    path('specialty/', SpecialityListAPIView.as_view(), name='specialty_list'),
    path('education/', EducationListAPIView.as_view(), name='education_list')
]