from django.contrib import admin
from .models import *


class UniversityImageInline(admin.TabularInline):
    model = UniversityImage
    extra = 1


class UnivDescriptionInline(admin.StackedInline):
    model = UnivDescription
    extra = 0


class HomeImageInline(admin.TabularInline):
    model = HomeImage
    extra = 1


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    inlines = [UniversityImageInline, UnivDescriptionInline]


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    inlines = [HomeImageInline]


admin.site.register(Country)
admin.site.register(Speciality)
admin.site.register(Education)
admin.site.register(Exam)
admin.site.register(StudentReview)
admin.site.register(Team)
admin.site.register(Consultation)
admin.site.register(AboutUs)
admin.site.register(CambrigeExam)
admin.site.register(StudyAbroadProgram)