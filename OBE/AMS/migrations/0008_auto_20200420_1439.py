# Generated by Django 3.0.3 on 2020-04-20 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMS', '0007_auto_20200420_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='Presence',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Not Registered', 'Not Registered')], max_length=20),
        ),
    ]
