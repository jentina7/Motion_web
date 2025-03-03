from rest_framework import serializers
from .models import *


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
    # нужно добавить exam
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