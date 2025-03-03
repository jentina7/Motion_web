from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(Speciality)
class StoreTranslationOptions(TranslationOptions):
    fields = ('speciality_name',)


@register(Education)
class ProductTranslationOptions(TranslationOptions):
    fields = ('education_name',)


@register(University)
class CountryTranslationOptions(TranslationOptions):
    fields = ('name', 'location')


@register(Exam)
class StoreTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Team)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'speciality')


@register(AboutUs)
class CountryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(CambrigeExam)
class StoreTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Home)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(StudyAbroadProgram)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')