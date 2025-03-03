from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, generics


class ConsultationForHomeCreateAPIView(generics.CreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationForHomeSerializer


class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class SpecialityListAPIView(generics.ListAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class EducationListAPIView(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class UniversityListAPIView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityListSerializer


class UnivDescriptionViewSet(viewsets.ModelViewSet):
    queryset = UnivDescription.objects.all()
    serializer_class = UnivDescriptionSerializer


class UniversityDetailListAPIView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityDetailSerializer