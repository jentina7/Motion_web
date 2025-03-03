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


class ConsultationForHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ["first_name", "contact"]


class HomeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeImage
        fields = ["image"]


class HomeSerializer(serializers.ModelSerializer):
    home_image = HomeImageSerializer(read_only=True)
    consultation = ConsultationForHomeSerializer()

    class Meta:
        model = Home
        fields = ["title", "description", "home_image", "consultation"]


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ["speciality_name"]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ["education_name"]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["country_name", "country_image"]


class UniversityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityImage
        fields = ["image"]


# country-detail
class UniversityListSerializer(serializers.ModelSerializer):
    univ_image = UniversityImageSerializer(many=True)

    class Meta:
        model = University
        fields = ["univ_image", "name", "location", "age"]


class UnivDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnivDescription
        fields = ["logo", "nominal_duration", "awards", "tuition_fee", "application_fee",
                  "registration_fee", "tuition_desc", "entry_qualication", "cost"]


class UniversityDetailSerializer(serializers.ModelSerializer):
    specialities = SpecialitySerializer(read_only=True, many=True)
    education = EducationSerializer(read_only=True, many=True)
    description = UnivDescriptionSerializer()
    univ_image = UniversityImageSerializer(many=True)

    class Meta:
        model = University
        fields = ["univ_image", "name", "location", "date_of_foundation", "programs", "specialities",
                  "languages", "education", "description"]