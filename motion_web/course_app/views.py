from rest_framework import serializers, generics, viewsets
from .serializers import *
from .models import *


class ExamListAPIView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamListSerializer


class ExamCreateAPIView(generics.CreateAPIView):
    serializer_class = ExamCreateSerializer


class ExamRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamDetailSerializer


class CambrigeExamListAPIView(generics.ListAPIView):
    queryset = CambrigeExam.objects.all()
    serializer_class = CambrigeExamSerializer


class CambrigeExamRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CambrigeExam.objects.all()
    serializer_class = CambrigeExamSerializer


class StudentReviewListAPIView(generics.ListAPIView):
    queryset = StudentReview.objects.all()
    serializer_class = StudentReviewSerializer


class StudentReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = StudentReviewCreateSerializer


class StudentReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentReview.objects.all()
    serializer_class = StudentReviewSerializer


class ConsultationListAPIView(generics.ListAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer


class ConsultationForHomeCreateAPIView(generics.CreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationForHomeSerializer


class HomeListAPIView(generics.ListAPIView):
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


class ConsultationCreateAPIView(generics.CreateAPIView):
    serializer_class = ConsultationCreateSerializer


class ConsultationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer


class TeamListAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamCreateAPIView(generics.CreateAPIView):
    serializer_class = TeamCreateSerializer


class TeamRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class AboutUsListAPIView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class AboutUsCreateAPIView(generics.CreateAPIView):
    serializer_class = AboutUsCreateSerializer


class AboutUsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class UniversityListAPIView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityListSerializer


class UnivDescriptionViewSet(viewsets.ModelViewSet):
    queryset = UnivDescription.objects.all()
    serializer_class = UnivDescriptionSerializer


class UniversityDetailListAPIView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityDetailSerializer