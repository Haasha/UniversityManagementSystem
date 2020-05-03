from django.urls import path
from . import views

urlpatterns = [
    path('StudentLogin/',views.StudentLogin, name='StudentLogin' ),
    path('StudentDashboard/',views.StudentDashboard, name='StudentDashboard' ),
    path('StudentCourseRegistration/',views.StudentCourseRegistration, name='StudentCourseRegistration' ),
    path('StudentLogout/',views.StudentLogout, name='StudentLogout' ),
    path('StudentAttendance/',views.StudentAttendance, name='StudentAttendance' ),
    path('StudentEvaluation/',views.StudentEvaluation, name='StudentEvaluation' ),
    path('StudentTranscript/',views.StudentTranscript, name='StudentTranscript' ),
    
    path('TeacherLogin/',views.TeacherLogin, name='TeacherLogin' ),
    
    path('TeacherEvaluation/',views.TeacherEvaluation, name='TeacherEvaluation' ),
    path('TeacherGrading/',views.TeacherGrading, name='TeacherGrading' ),
    path('TeacherEvaluation/Mod/',views.TeacherEvaluationMod, name='TeacherEvaluationMod' ),
    path('TeacherEvaluation/Mod/Insert/',views.TeacherEvaluationModInsert, name='TeacherEvaluationModInsert' ),
    path('TeacherEvaluation/Mod/Update/',views.TeacherEvaluationModUpdate, name='TeacherEvaluationModUpdate' ),
    path('TeacherEvaluation/Mod/Update/Save/',views.TeacherEvaluationModUpdateSave, name='TeacherEvaluationModUpdateSave' ),
    path('TeacherEvaluation/Mod/Insert/Save/',views.TeacherEvaluationModInsertSave, name='TeacherEvaluationModInsertSave' ),
    
    path('TeacherAttendance/',views.TeacherAttendance, name='TeacherAttendance' ),
    path('TeacherAttendance/Mod/',views.TeacherAttendanceMod, name='TeacherAttendanceMod' ),
    path('TeacherAttendance/Mod/Insert/',views.TeacherAttendanceModInsert, name='TeacherAttendanceModInsert' ),
    path('TeacherAttendance/Mod/Update/',views.TeacherAttendanceModUpdate, name='TeacherAttendanceModUpdate' ),
    path('TeacherAttendance/Mod/Insert/Save/',views.TeacherAttendanceModInsertSave, name='TeacherAttendanceModInsertSave' ),
    path('TeacherAttendance/Mod/Update/Save/',views.TeacherAttendanceModUpdateSave, name='TeacherAttendanceModUpdateSave' ),
    
    path('TeacherDashboard/',views.TeacherDashboard, name='TeacherDashboard' ),
    path('TeacherLogout/',views.TeacherLogout, name='TeacherLogout' ),

]

"""path('TeacherLogin/', views.TeacherLogin, name='TeacherLogin' ),
    path('home/', views.TeacherLogin, name='AMS-home'),
    path('logout/', views.logout, name = 'logout'),"""
