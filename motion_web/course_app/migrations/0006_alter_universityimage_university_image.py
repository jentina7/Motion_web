# Generated by Django 5.1.6 on 2025-03-03 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0005_alter_univdescription_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universityimage',
            name='university_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='univ_image', to='course_app.university'),
        ),
    ]
