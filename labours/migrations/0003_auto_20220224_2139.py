# Generated by Django 2.2.10 on 2022-02-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labours', '0002_auto_20220224_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labour',
            name='mobile',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
