# Generated by Django 5.0.7 on 2024-09-30 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0002_addcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcourse',
            name='section',
            field=models.CharField(choices=[('S1', 'Section1'), ('S2', 'Section2'), ('S4', 'Section4'), ('S3', 'Section3')], max_length=50),
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]