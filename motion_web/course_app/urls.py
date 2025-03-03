from .views import *
from django.urls import path, include
from .views import *

urlpatterns = [
    path('exam/', ExamListAPIView.as_view(), name='exam_list'),
    path('exam_create/', ExamCreateAPIView.as_view(), name='exam_create'),
    path('exam/<int:pk>/', ExamRetrieveUpdateDestroyAPIView.as_view(), name='exam_detail'),

    path('cambrige_exam/', CambrigeExamListAPIView.as_view(), name='cambrige_exam_list'),
    path('cambrige_exam/<int:pk>/', CambrigeExamRetrieveUpdateDestroyAPIView.as_view(), name='cambrige_exam_detail'),

    path('review/', StudentReviewListAPIView.as_view(), name='review_list'),
    path('review_create/', StudentReviewCreateAPIView.as_view(), name='review_create'),
    path('review/<int:pk>/', StudentReviewRetrieveUpdateDestroyAPIView.as_view(), name='review_detail'),

    path('consultation/', ConsultationListAPIView.as_view(), name='consultation_list'),
    path('consultation_create/', ConsultationCreateAPIView.as_view(), name='consultation_create'),
    path('consultation/<int:pk>/', ConsultationRetrieveUpdateDestroyAPIView.as_view(), name='consultation_detail'),

    path('team/', TeamListAPIView.as_view(), name='team_list'),
    path('team_create/', TeamCreateAPIView.as_view(), name='team_create'),
    path('team/<int:pk>/', TeamRetrieveUpdateDestroyAPIView.as_view(), name='team_detail'),

    path('about_us/', AboutUsListAPIView.as_view(), name='about_us_list'),
    path('about_us_create/', AboutUsCreateAPIView.as_view(), name='about_us_create'),
    path('about_us/<int:pk>/', AboutUsRetrieveUpdateDestroyAPIView.as_view(), name='about_us_detail'),

    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('home/', HomeListAPIView.as_view(), name='home_list'),
    path('country/<int:pk>/', UniversityListAPIView.as_view(), name='country_detail'),
    path('university/<int:pk>/', UniversityDetailListAPIView.as_view(), name='university_detail'),
    path('consultation_for_home/', ConsultationForHomeCreateAPIView.as_view(), name='consultation_for_home'),
    path('specialty/', SpecialityListAPIView.as_view(), name='specialty_list'),
    path('education/', EducationListAPIView.as_view(), name='education_list')
]