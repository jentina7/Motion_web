from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


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

# Модель экзаменов
class Exam(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    exam_image = models.ImageField(upload_to='exam_images/')
    exam_type = models.CharField(max_length=100, choices=[
        ('IELTS', 'IELTS'),
        ('Aptis', 'Aptis'),
        ('Other', 'Other'),
    ])

    def str(self):
        return self.name


# Модель отзыва студента
class StudentReview(models.Model):
    video_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


# Модель заявки на консультацию
class Consultation(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    contact = PhoneNumberField(region='KG', null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Заявка от {self.name} ({self.phone})"

# модель команды (про нас)
class Team(models.Model):
    name = models.CharField(max_length=150)
    speciality = models.CharField(max_length=200)
    team_image = models.ImageField(upload_to='team_images/')

# модель информации про курс
class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='exam_images/')
    our_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='our_teams')


class CambrigeExam(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    exam_image = models.ImageField(upload_to='cambrige_exam_images/')



class Home(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Модель программы обучения за границей
class StudyAbroadProgram(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='study_images/')

    def str(self):
        return self.title


class HomeImage(models.Model):
    home_image = models.ForeignKey(Home, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="image/")




