from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


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
class UniversityAdmin(TranslationAdmin):
    inlines = [UniversityImageInline, UnivDescriptionInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Home)
class HomeAdmin(TranslationAdmin):
    inlines = [HomeImageInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Country, Speciality, Education, Exam, Team, AboutUs, CambrigeExam, StudyAbroadProgram)
class AllAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(StudentReview)
admin.site.register(Consultation)
