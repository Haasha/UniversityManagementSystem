# Generated by Django 3.0.3 on 2020-04-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMS', '0006_auto_20200420_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='Duration',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('SemesterID', 'BatchID', 'CourseID', 'Section', 'StudentID', 'LectureNo')},
        ),
        migrations.AlterUniqueTogether(
            name='courseregistered',
            unique_together={('SemesterID', 'BatchID', 'CourseID', 'Section', 'StudentID')},
        ),
        migrations.AlterUniqueTogether(
            name='courseregistration',
            unique_together={('SemesterID', 'BatchID', 'CourseID', 'Section')},
        ),
        migrations.AlterUniqueTogether(
            name='evaluation',
            unique_together={('SemesterID', 'BatchID', 'CourseID', 'Section', 'StudentID', 'EvaluationNumber')},
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='ProgramID',
        ),
        migrations.RemoveField(
            model_name='courseregistered',
            name='ProgramID',
        ),
        migrations.RemoveField(
            model_name='courseregistration',
            name='ProgramID',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='ProgramID',
        ),
    ]
