# Generated by Django 3.0.3 on 2020-03-28 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('BatchID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Recruitment_Date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('CourseID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.CharField(blank=True, max_length=200, null=True)),
                ('CreditHours', models.PositiveSmallIntegerField()),
                ('PreReq', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AMS.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('DeptID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Desc', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('ProgramID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('MinSemesters', models.PositiveSmallIntegerField()),
                ('MaxSemesters', models.PositiveSmallIntegerField()),
                ('DepartmentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('SemesterID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Start_Date', models.DateField()),
                ('End_Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('StudentID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('DoB', models.DateField(blank=True, null=True)),
                ('CNIC', models.CharField(blank=True, max_length=13, null=True)),
                ('Password', models.CharField(max_length=200)),
                ('Gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10, null=True)),
                ('PhoneNo', models.CharField(blank=True, max_length=11, null=True)),
                ('Section', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S', 'S'), ('T', 'T'), ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y'), ('Z', 'Z')], max_length=1, null=True)),
                ('Status', models.CharField(blank=True, choices=[('1', 'Current'), ('2', 'Graduated')], max_length=20, null=True)),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
                ('PostalCode', models.CharField(blank=True, max_length=5, null=True)),
                ('City', models.CharField(blank=True, max_length=50, null=True)),
                ('BatchID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Batch')),
                ('ProgramID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Program')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Designation', models.CharField(blank=True, choices=[('A', 'Lecturer'), ('B', 'Associate Professor'), ('C', 'Assistant Professor'), ('D', 'Professor')], max_length=20, null=True)),
                ('Password', models.CharField(max_length=200)),
                ('Gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10, null=True)),
                ('PhoneNo', models.CharField(blank=True, max_length=11, null=True)),
                ('HireDate', models.DateField()),
                ('Salary', models.IntegerField()),
                ('DeptID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Department')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramOutline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SemesterNumber', models.PositiveSmallIntegerField()),
                ('CourseType', models.CharField(choices=[('1', 'Core'), ('2', 'Elective')], max_length=20)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Course')),
                ('ProgramID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Program')),
            ],
            options={
                'unique_together': {('ProgramID', 'SemesterNumber', 'CourseID')},
            },
        ),
        migrations.CreateModel(
            name='CourseRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S', 'S'), ('T', 'T'), ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y'), ('Z', 'Z')], max_length=1)),
                ('CourseType', models.CharField(choices=[('1', 'Core'), ('2', 'Elective')], max_length=20, null=True)),
                ('SeatsLeft', models.PositiveIntegerField()),
                ('Description', models.CharField(max_length=100)),
                ('BatchID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Batch')),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Course')),
                ('EmployeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Employee')),
                ('ProgramID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Program')),
                ('SemesterID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Semester')),
            ],
            options={
                'unique_together': {('SemesterID', 'ProgramID', 'BatchID', 'CourseID', 'Section', 'EmployeeID')},
            },
        ),
        migrations.CreateModel(
            name='CourseRegistered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S', 'S'), ('T', 'T'), ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y'), ('Z', 'Z')], max_length=1, null=True)),
                ('Grade', models.CharField(choices=[('1', 'A+'), ('2', 'A'), ('3', 'A-'), ('4', 'B+'), ('5', 'B'), ('6', 'B-'), ('7', 'C+'), ('8', 'C'), ('9', 'C-'), ('10', 'D+'), ('11', 'D'), ('12', 'F'), ('13', 'W'), ('14', 'I')], max_length=4)),
                ('BatchID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Batch')),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Course')),
                ('EmployeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Employee')),
                ('ProgramID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Program')),
                ('SemesterID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Semester')),
                ('StudentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Student')),
            ],
            options={
                'unique_together': {('SemesterID', 'ProgramID', 'BatchID', 'CourseID', 'Section', 'EmployeeID', 'StudentID')},
            },
        ),
        migrations.CreateModel(
            name='CLO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CLO_ID', models.CharField(max_length=3)),
                ('CLO_Desc', models.CharField(blank=True, max_length=200, null=True)),
                ('CLO_Category', models.CharField(choices=[('1', 'Affective'), ('2', 'Cognitive'), ('1', 'Psychomotor')], max_length=50)),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMS.Course')),
            ],
            options={
                'unique_together': {('CourseID', 'CLO_ID')},
            },
        ),
    ]
