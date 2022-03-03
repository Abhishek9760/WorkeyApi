# Generated by Django 2.2.10 on 2022-02-24 16:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.MaxLengthValidator(20), django.core.validators.MinLengthValidator(3)]),
        ),
    ]
