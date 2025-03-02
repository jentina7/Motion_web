from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Модель программы обучения за границей
class StudyAbroadProgram(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='study_images/')

    def str(self):
        return self.title


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







