# Generated by Django 3.0.3 on 2020-04-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMS', '0008_auto_20200420_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseregistered',
            name='Grade',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'), ('D+', 'D+'), ('D', 'D'), ('F', 'F'), ('W', 'W'), ('I', 'I')], max_length=4),
        ),
        migrations.AlterField(
            model_name='courseregistration',
            name='CourseType',
            field=models.CharField(choices=[('Core', 'Core'), ('Elective', 'Elective')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='programoutline',
            name='CourseType',
            field=models.CharField(choices=[('Core', 'Core'), ('Elective', 'Elective')], max_length=20),
        ),
    ]