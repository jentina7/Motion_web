# Generated by Django 5.1.6 on 2025-03-03 05:29

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CambrigeExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('exam_image', models.ImageField(upload_to='cambrige_exam_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('exam_image', models.ImageField(upload_to='exam_images/')),
                ('exam_type', models.CharField(choices=[('IELTS', 'IELTS'), ('Aptis', 'Aptis'), ('Other', 'Other')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudentReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudyAbroadProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='study_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('speciality', models.CharField(max_length=200)),
                ('team_image', models.ImageField(upload_to='team_images/')),
            ],
        ),
        migrations.AddField(
            model_name='univdescription',
            name='cost',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='consultation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course_app.consultation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='exam',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course_app.exam'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='exam_images/')),
                ('our_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='our_teams', to='course_app.team')),
            ],
        ),
    ]
