# Generated by Django 5.0.7 on 2024-10-15 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_uploadedfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlist',
            name='Register_Number',
            field=models.CharField(max_length=100),
        ),
    ]
