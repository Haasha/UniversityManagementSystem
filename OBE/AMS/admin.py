from django.contrib import admin
# Register your models here.
from .resource import *

"""@admin.register(Department,Program,Course,Semester,ProgramOutline,Student,Employee,CourseRegistration)
class ViewAdmin(ImportExportModelAdmin):
	pass

class BatchResource(resources.ModelResource):
	class Meta:
		model=Batch
		import_id_fields = ('BatchID', 'Name','Recruitment_Date',)

class BatchAdmin(ImportExportModelAdmin):
        resource_class = BatchResource

"""

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Program,ProgramAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Semester,SemesterAdmin)
admin.site.register(ProgramOutline,ProgramOutlineAdmin)
admin.site.register(Batch,BatchAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(CourseRegistration,CourseRegistrationAdmin)
admin.site.register(CourseRegistered,CourseRegisteredAdmin)
admin.site.register(Evaluation)
admin.site.register(Attendance)

