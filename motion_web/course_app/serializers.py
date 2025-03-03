from rest_framework import serializers
from .models import *

# Exam


class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['exam_type', 'name', 'description', 'exam_image']


class ExamDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['name', 'description', 'exam_image']


class ExamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

# cambrige


class CambrigeExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = CambrigeExam
        fields = ['name', 'description', 'exam_image']


# StudentReview
class StudentReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentReview
        fields = ['video_url', 'created_at']


class StudentReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentReview
        fields = '__all__'


class ConsultationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['first_name', 'last_name', 'contact', 'email', 'message']


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'speciality', 'team_image']


class AboutUsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['title', 'description', 'image', 'our_team']


class StudyAbroadProgramCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyAbroadProgram
        fields = '__all__'


class StudyAbroadProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyAbroadProgram
        fields = ['title', 'description', 'image', 'our_team']



