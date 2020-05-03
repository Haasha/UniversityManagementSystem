from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import *

class DepartmentResource(resources.ModelResource):
	class Meta:
		model=Department
		import_id_fields = ('DeptID', 'Name','Desc',)
class DepartmentAdmin(ImportExportModelAdmin):
        resource_class = DepartmentResource

class ProgramResource(resources.ModelResource):
	class Meta:
		model=Program
		import_id_fields = ('ProgramID', 'Name','DepartmentID','MinSemesters','MaxSemesters',)
class ProgramAdmin(ImportExportModelAdmin):
        resource_class = ProgramResource

class CourseResource(resources.ModelResource):
	class Meta:
		model=Course
		import_id_fields = ('CourseID', 'Title','Description','CreditHours','PreReq',)
class CourseAdmin(ImportExportModelAdmin):
        resource_class = CourseResource

class SemesterResource(resources.ModelResource):
	class Meta:
		model=Semester
		import_id_fields = ('SemesterID', 'Name','Start_Date','End_Date',)
class SemesterAdmin(ImportExportModelAdmin):
        resource_class = SemesterResource

class ProgramOutlineResource(resources.ModelResource):
	class Meta:
		model=ProgramOutline
		import_id_fields = ('ProgramID', 'SemesterNumber','CourseID','CourseType','Description',)
class ProgramOutlineAdmin(ImportExportModelAdmin):
        resource_class = ProgramOutlineResource

class BatchResource(resources.ModelResource):
	class Meta:
		model=Batch
		import_id_fields = ('BatchID', 'Name','Recruitment_Date',)
class BatchAdmin(ImportExportModelAdmin):
        resource_class = BatchResource

class StudentResource(resources.ModelResource):
	class Meta:
		model=Student
		import_id_fields = ('StudentID', 'Name','Email','DoB','CNIC','Password','Gender','PhoneNo','ProgramID','BatchID','Section','Status',)
class StudentAdmin(ImportExportModelAdmin):
        resource_class = StudentResource

class EmployeeResource(resources.ModelResource):
	class Meta:
		model=Employee
		import_id_fields = ('EmployeeID', 'Name','Email','Designation','Password','Gender','PhoneNo','HireDate','Salary','DeptID',)
class EmployeeAdmin(ImportExportModelAdmin):
        resource_class = EmployeeResource

class CourseRegistrationResource(resources.ModelResource):
	class Meta:
		model=CourseRegistration
		import_id_fields = ('id','SemesterID','BatchID','CourseID','Section','EmployeeID','CourseType','SeatsLeft','Description',)
class CourseRegistrationAdmin(ImportExportModelAdmin):
        resource_class = CourseRegistrationResource

class CourseRegisteredResource(resources.ModelResource):
	class Meta:
		model=CourseRegistered
		import_id_fields = ('id','SemesterID','BatchID','CourseID','Section','StudentID','Grade',)
class CourseRegisteredAdmin(ImportExportModelAdmin):
        resource_class = CourseRegisteredResource
