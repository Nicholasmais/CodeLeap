# Generated by Django 4.2 on 2025-01-08 18:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_career_created_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
