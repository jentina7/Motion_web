from rest_framework import serializers, generics
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

