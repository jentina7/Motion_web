from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Home(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # consultation = models.ForeignKey()
    # exam = models.For

    def __str__(self):
        return self.title


class HomeImage(models.Model):
    home_image = models.ForeignKey(Home, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="image/")


class Country(models.Model):
    country_name = models.CharField(max_length=60)
    country_image = models.ImageField(upload_to='country_images/')

    def __str__(self):
        return self.country_name

class Speciality(models.Model):
    speciality_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.speciality_name


class Education(models.Model):
    education_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.education_name


class UnivDescription(models.Model):
    logo = models.ImageField(verbose_name="logo/")
    nominal_duration = models.CharField(max_length=40)
    awards = models.TextField()
    tuition_fee = models.CharField(max_length=60)
    application_fee = models.CharField(max_length=60)
    registration_fee = models.CharField(max_length=60)
    tuition_desc = models.TextField()
    entry_qualication = models.TextField()

    def __str__(self):
        return


class University(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="univ_country")
    name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(70)],
                                           null=True, blank=True)
    date_of_foundation = models.DateField(auto_now=True)
    programs = models.TextField()
    specialities = models.ManyToManyField(Speciality)
    languages = models.CharField(max_length=100)
    education = models.ManyToManyField(Education)
    description = models.ForeignKey(UnivDescription, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UniversityImage(models.Model):
    university_image = models.ForeignKey(University, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="image/")

