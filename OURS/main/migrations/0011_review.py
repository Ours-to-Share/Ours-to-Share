# Generated by Django 3.2.5 on 2021-09-08 09:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_classroom_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutor_review_score', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('tutor_review_time', models.DateTimeField(blank=True, null=True)),
                ('student_review_score', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('student_review_time', models.DateTimeField(blank=True, null=True)),
                ('classroom', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.classroom')),
            ],
        ),
    ]