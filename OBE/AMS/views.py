from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
import numpy as np
from AMS.models import *

def StudentLogin(request):
	if request.session.has_key('StudentID'):
		return HttpResponseRedirect(reverse('StudentDashboard'))
	else:
		if request.method=='POST':
			form=request.POST
			Result=Student.objects.filter(StudentID=form.get('ID'), Password=form.get('Password'))
			if not Result:
				return render(request,'AMS/StudentLogin.html')	
			else:
				ID=form.get('ID')
				request.session['StudentID']=ID
				return HttpResponseRedirect(reverse('StudentDashboard'))
		return render(request,'AMS/StudentLogin.html')

def StudentDashboard(request):
	if request.session.has_key('StudentID'):
		ID = request.session['StudentID']
		context={ 'Students' : Student.objects.get(StudentID=ID)}
		return render(request, 'AMS/StudentDashboard.html',context)
	else:
		return HttpResponseRedirect(reverse('StudentLogin'))
def Score(Grade):
	if Grade=='A+':
		return 4.0
	elif Grade=='A':
		return 4.0
	elif Grade=='A-':
		return 3.67
	elif Grade=='B+':
		return 3.33
	elif Grade=='B':
		return 3.0
	elif Grade=='B-':
		return 2.67
	elif Grade=='C+':
		return 2.33
	elif Grade=='C':
		return 2.0
	elif Grade=='C-':
		return 1.67
	elif Grade=='D+':
		return 1.33
	elif Grade=='D':
		return 1.0
	elif Grade=='F':
		return 0.0
	elif Grade=='W':
		return 0.0
	elif Grade=='I':
		return 0
def StudentTranscript(request):
	if request.session.has_key('StudentID'):
		ID = request.session['StudentID']
		Objects=CourseRegistered.objects.filter(StudentID=ID).order_by('SemesterID','CourseID')
		Semesters=[]
		SGPAs=[]
		CGPAs=[]
		Courses=[]
		CoursesNames=[]
		CreditHour=[]
		Types=[]
		Grades=[]
		Points=[]
		for i in Objects:
			if str(i.SemesterID) not in Semesters:
				Semesters.append(str(i.SemesterID))
				Courses.append([])
				Grades.append([])
				CGPAs.append(0.0)
				SGPAs.append(0.0)
			Index=Semesters.index(str(i.SemesterID))
			Courses[Index].append(str(i.CourseID))
			Grades[Index].append(i.Grade)
		for i in range(len(Courses)):
			CreditHour.append([])
			CoursesNames.append([])
			Types.append([])
			for j in range(len(Courses[i])):
				Temp=Course.objects.get(CourseID=Courses[i][j])
				CreditHour[i].append(Temp.CreditHours)
				CoursesNames[i].append(Temp.Title)

		OverallPoints=0
		OverallCreditHours=0
		for i in range(len(Semesters)):
			TempCreditHours=0
			TempPoints=0
			Points.append([])
			for j in range(len(Courses[i])):
				Points[i].append(Score(Grades[i][j]))
				if Points[i][j]!=0:
					TempPoints+=(Points[i][j]*CreditHour[i][j])
					TempCreditHours+=CreditHour[i][j]
			OverallPoints+=TempPoints
			OverallCreditHours+=TempCreditHours
			if TempCreditHours==0:
				SGPAs[i]=0.0
				if i>0 :
					CGPAs[i]=CGPAs[i-1]
				else:
					CGPAs[i]=0.00
			else:
				SGPAs[i]=round(TempPoints/TempCreditHours,3)
				CGPAs[i]=round(OverallPoints/OverallCreditHours,3)
		Results=[]
		for i in range(len(Courses)):
			Results.append(zip(Courses[i],CoursesNames[i],CreditHour[i],Grades[i],Points[i]))
		Context={
			'Semesters':zip(Semesters,SGPAs,CGPAs,Results)
		}
		return render(request,'AMS/StudentTranscript.html',Context)
		return HttpResponseRedirect(reverse('StudentDashboard'))
	else:
		return HttpResponseRedirect(reverse('StudentLogin'))
def StudentAttendance(request):
	if request.session.has_key('StudentID'):
		ID=request.session['StudentID']
		if request.method=='POST':
			Sem=form.get('Sem')
		else:
			Sem=Semester.objects.order_by('Start_Date').reverse()[0]
		
		Objects=Attendance.objects.filter(SemesterID=Sem,StudentID=ID)
		Courses=[]
		Attendances=[]
		Durations=[]
		Weightages=[]
		Dates=[]
		for i in Objects:
			if i.CourseID not in Courses:
				Courses.append(i.CourseID)
				Attendances.append([])
				Durations.append([])
				Dates.append([])
				Weightages.append(0.0)

			Index=Courses.index(i.CourseID)
			if i.LectureNo>1:
				Dates[Index].append(i.Date)
				Attendances[Index].append(i.Presence)
				Durations[Index].append(i.Duration)
				Weightages[Index]+=(1*i.Duration)
		Percentages=[]
		for i in range(len(Courses)):
			if len(Durations[i])<1:
				Percentages.append(100)
			else:
				Score=np.sum(Durations[i])
				Percentages.append(0.0)
				for j in range(len(Attendances[i])):
					if Attendances[i][j]=='Present' or Attendances[i][j]=='Not Registered':
						Percentages[i]+=Durations[i][j]
				Percentages[i]*=(100/Score)
				Percentages[i]=round(Percentages[i],2)
		Results=[]
		for i in range(len(Durations)):
			Results.append(zip(Dates[i],Durations[i],Attendances[i]))
		Context={
			'Records':zip(Courses,Percentages),
			'Results':Results
		}
		return render(request,'AMS/StudentAttendance.html',Context)
	else:
		return HttpResponseRedirect(reverse('StudentLogin'))

def StudentEvaluation(request):
	if request.session.has_key('StudentID'):
		ID=request.session['StudentID']
		if request.method=='POST':
			Sem=form.get('Sem')
		else:
			Sem=Semester.objects.order_by('Start_Date').reverse()[0]
		print('\n\n\nFILTERING OBJECTS NOW:')
		Objects=Evaluation.objects.filter(SemesterID=Sem,StudentID=ID).order_by('CourseID','Type')
		print(Objects,'\n\n\n')
		
		Courses=[]
		Weightages=[]
		TotalMarks=[]
		ObtainedMarks=[]
		Types=[]
		
		for i in Objects:
			if str(i.CourseID) not in Courses:
				Courses.append(str(i.CourseID))
				Weightages.append([])
				TotalMarks.append([])
				ObtainedMarks.append([])
				Types.append([])
			Index=Courses.index(str(i.CourseID))
			if i.EvaluationNumber>1:
				Weightages[Index].append(i.Weightage)
				TotalMarks[Index].append(i.TotalMarks)
				ObtainedMarks[Index].append(i.ObtainedMarks)
				Types[Index].append(i.Type)
		TotalAbs=[]
		TotalObtainedAbs=[]
		Temp=0
		for i in range(len(Courses)):
			if len(Weightages[i])>0:
				TotalAbs.append(np.sum(Weightages[i]))
				TotalObtainedAbs.append(np.sum([ x*y for x,y in zip(Weightages[i],[x/y for x, y in zip(ObtainedMarks[i], TotalMarks[i])]) ]) )
			else:
				TotalAbs.append(0.0)
				TotalObtainedAbs.append(0.0)
		print(Courses,TotalAbs,TotalObtainedAbs,Weightages,TotalMarks,ObtainedMarks,'\n\n\n')
		
		Results=[]
		for i in range(len(Weightages)):
			Results.append(zip(Weightages[i],TotalMarks[i],ObtainedMarks[i],Types[i]))
		print(Results)
		Context={
			'Courses':Courses,
			'Results':zip(TotalAbs,TotalObtainedAbs,Results)
		}
		"""
			Index=Courses.index(i.CourseID)
			if i.LectureNo>1:
				Dates[Index].append(i.Date)
				Attendances[Index].append(i.Presence)
				Durations[Index].append(i.Duration)
				Weightages[Index]+=(1*i.Duration)
		Percentages=[]
		for i in range(len(Courses)):
			if len(Durations[i])<1:
				Percentages.append(100)
			else:
				Score=np.sum(Durations[i])
				Percentages.append(0.0)
				for j in range(len(Attendances[i])):
					if Attendances[i][j]=='Present' or Attendances[i][j]=='Not Registered':
						Percentages[i]+=Durations[i][j]
				Percentages[i]*=(100/Score)
				Percentages[i]=round(Percentages[i],2)
		Results=[]
		for i in range(len(Durations)):
			Results.append(zip(Dates[i],Durations[i],Attendances[i]))"""

		return render(request,'AMS/StudentEvaluation.html',Context)
		return HttpResponseRedirect(reverse('StudentDashboard'))
	else:
		return HttpResponseRedirect(reverse('StudentLogin'))

def StudentCourseRegistration(request):
	if request.session.has_key('StudentID'):
		if request.method=='POST':
			ID = request.session['StudentID']
			form=request.POST
			StudentRecord=Student.objects.get(StudentID=ID)
			SemID= Semester.objects.order_by('Start_Date').reverse()[0]
			CourseRegistrations=CourseRegistration.objects.filter(SemesterID=SemID.SemesterID,BatchID=StudentRecord.BatchID)
			List=[]
			for i in CourseRegistrations:
				if i.CourseID not in List:
					List.append(i.CourseID)

			for i in range(len(List)):

				if form.get("Attendance_"+str(i+1))=="on":
					y=CourseRegistered(SemesterID=SemID,BatchID=StudentRecord.BatchID,CourseID=List[i],Section=form.get("Section_"+str(i+1)),StudentID=StudentRecord,Grade="I")
					y.save()
					y=Evaluation(SemesterID=SemID,BatchID=StudentRecord.BatchID,CourseID=List[i],Section=form.get("Section_"+str(i+1)),StudentID=StudentRecord,EvaluationNumber=1,Weightage=0,ObtainedMarks=0,TotalMarks=0)
					y.save()
					y=Attendance(SemesterID=SemID,BatchID=StudentRecord.BatchID,CourseID=List[i],Section=form.get("Section_"+str(i+1)),StudentID=StudentRecord,LectureNo=1,Duration=0,Presence='Present')
					y.save()
			return HttpResponseRedirect(reverse('StudentCourseRegistration'))
		else:
			ID = request.session['StudentID']
			StudentRecord=Student.objects.get(StudentID=ID)
			SemID= Semester.objects.order_by('Start_Date').reverse()[0].SemesterID
			CourseRegistrations=CourseRegistration.objects.filter(SemesterID=SemID,BatchID=StudentRecord.BatchID)
			List=[]
			Sections=[]
			for i in CourseRegistrations:
				if i.CourseID not in List:
					Sections.append([])
					List.append(i.CourseID)
				Sections[len(List)-1].append(i.Section)

			Courses=Course.objects.filter(pk__in=List)

			CoursesRegistered=CourseRegistered.objects.filter(SemesterID=SemID,BatchID=StudentRecord.BatchID,StudentID=ID)
			Status=[]
			for i in range(len(List)):
				Status.append('UnRegistered')
			for i in CoursesRegistered:
				Status[List.index(i.CourseID)]='Registered'
			context={
				'Records':zip(CourseRegistrations,Courses,Sections,Status),
			}
			return render(request, 'AMS/course_registration.html',context)
	else:
		return HttpResponseRedirect(reverse('StudentLogin'))

def StudentLogout(request):
	try:
		del request.session['StudentID']
	except:
		pass
	return HttpResponseRedirect(reverse('StudentLogin'))


def TeacherLogin(request):
	if request.session.has_key('EmpID'):
		return HttpResponseRedirect(reverse('TeacherDashboard'))
	else:
		if request.method=='POST':
			form=request.POST
			Result=Employee.objects.filter(EmployeeID=form.get('ID'), Password=form.get('Password'))
			if not Result:
				return render(request,'AMS/TeacherLogin.html')
			else:
				ID=form.get('ID')
				request.session['EmpID']=ID
				return HttpResponseRedirect(reverse('TeacherDashboard'))
		else:
			return render(request,'AMS/TeacherLogin.html')

def TeacherDashboard(request):
	if request.session.has_key('EmpID'):
		ID = request.session['EmpID']
		context={ 'Employee' : Employee.objects.get(EmployeeID=ID)}
		return render(request, 'AMS/TeacherDashboard.html',context)
	else:
		return HttpResponseRedirect(reverse('TeacherLogin'))

def TeacherLogout(request):
	try:
		del request.session['EmpID']
	except:
		pass
	return HttpResponseRedirect(reverse('TeacherLogin'))

def TeacherAttendance(request):

	if request.session.has_key('EmpID'):
		ID = request.session['EmpID']
		SemID= Semester.objects.order_by('Start_Date').reverse()[0]
		Data=CourseRegistration.objects.filter(SemesterID=SemID, EmployeeID=ID)
		Batches=[]
		Courses=[]
		Sections=[]
		for i in Data:
			if i.BatchID not in Batches:
				Batches.append(i.BatchID)
			if i.CourseID not in Courses:
				Courses.append(i.CourseID)
			if i.Section not in Sections:
				Sections.append(i.Section)
		Context={
			'Batches':Batches,
			'Courses':Courses,
			'Sections':Sections
		}
		return render(request,'AMS/TeacherAttendance.html',Context)
	else:
		return HttpResponseRedirect(reverse('TeacherLogin'))

def TeacherEvaluation(request):
	if request.session.has_key('EmpID'):
		ID = request.session['EmpID']
		SemID= Semester.objects.order_by('Start_Date').reverse()[0]
		Data=CourseRegistration.objects.filter(SemesterID=SemID, EmployeeID=ID)
		Batches=[]
		Courses=[]
		Sections=[]
		for i in Data:
			if i.BatchID not in Batches:
				Batches.append(i.BatchID)
			if i.CourseID not in Courses:
				Courses.append(i.CourseID)
			if i.Section not in Sections:
				Sections.append(i.Section)
		Context={
			'Batches':Batches,
			'Courses':Courses,
			'Sections':Sections
		}
		return render(request,'AMS/TeacherEvaluation.html',Context)
	else:
		return HttpResponseRedirect(reverse('TeacherLogin'))

def TeacherEvaluationModInsert(request):
	if request.session.has_key('EmpID'):
		if request.method=='POST':
			form=request.POST
			Sem= Semester.objects.get(SemesterID=form.get('Sem'))
			batch=Batch.objects.get(BatchID=form.get('Batch'))
			course=Course.objects.get(CourseID=form.get('Course'))
			Section=form.get('Section')
			Weightage=float(form.get('Weightage'))
			TotalMarks=float(form.get('TotalMarks'))
			Type=form.get('Type')
			Students=CourseRegistered.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section)
			Objects=Evaluation.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section).order_by('EvaluationNumber').reverse()
			if not Objects:
				Count=0
			else:
				Count=Objects[0].EvaluationNumber
			for i in range(len(Students)):
				New=Evaluation(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section,StudentID=Students[i].StudentID,EvaluationNumber=Count+1,Weightage=Weightage,TotalMarks=TotalMarks,ObtainedMarks=0.0,Type=Type)
				New.save()
			return TeacherEvaluationModUpdate(request)
		return HttpResponseRedirect(reverse('TeacherEvaluation'))
	else:
		return HttpResponseRedirect(reverse('TeacherLogin'))

def TeacherEvaluationModUpdate(request):
	if request.session.has_key('EmpID'):
		if request.method=='POST':
			form=request.POST
			
			Sem= Semester.objects.get(SemesterID=form.get('Sem'))
			batch=Batch.objects.get(BatchID=form.get('Batch'))
			course=Course.objects.get(CourseID=form.get('Course'))
			Section=form.get('Section')
			if  form.get('Weightage') and form.get('TotalMarks'):
				Weightage=float(form.get('Weightage'))
				TotalMarks=float(form.get('TotalMarks'))
				Type=form.get('Type')
				EvalNum=Evaluation.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section).order_by('EvaluationNumber').reverse()
				EvalNum=EvalNum[0].EvaluationNumber
			else:
				EvalNum=int(form.get('EvalNum'))
				Object=Evaluation.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section,EvaluationNumber=EvalNum).reverse()[0]
				Weightage=Object.Weightage
				TotalMarks=Object.TotalMarks
				Type=Object.Type
			Data=Evaluation.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section,EvaluationNumber=EvalNum)
			if Data:
				Students=CourseRegistered.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section)
				Names=[]
				StudentIDs=[]
				ObtainedMarks=[]
				for i in Data:
					if i.StudentID not in StudentIDs:
						StudentIDs.append(i.StudentID)
						ObtainedMarks.append(i.ObtainedMarks)
				Names=Student.objects.filter(pk__in=StudentIDs)
				Choices=['Assignment','Quiz','Mid Exam','Lab Task','Final Exam']
				Context={
					'Records':zip(StudentIDs,Names,ObtainedMarks),
					'Semester':form.get('Sem'),
					'Batch':batch,
					'Course': course,
					'Section': Section,
					'Weightage':Weightage,
					'TotalMarks':TotalMarks,
					'EvalNum':EvalNum,
					'Type':Type,
					'Choices':Choices
				}
				return render(request,'AMS/UpdateEvaluation.html',Context)
			else:
				return HttpResponseRedirect(reverse('TeacherEvaluation'))
		else:
			return 	HttpResponseRedirect(reverse('TeacherEvaluation'))
	else:
		return HttpResponseRedirect(reverse('TeacherLogin'))	
def TeacherEvaluationModUpdateSave(request):
	if request.session.has_key('EmpID'):
		if request.method=='POST':
			form=request.POST
			Sem= Semester.objects.get(SemesterID=form.get('Sem'))
			batch=Batch.objects.get(BatchID=form.get('Batch'))
			course=Course.objects.get(CourseID=form.get('Course'))
			Section=form.get('Section')
			EvalNum=int(form.get('EvalNum'))
			Weightage=float(form.get('Weightage'))
			TotalMarks=float(form.get('TotalMarks'))
			Type=form.get('Type')
			Students=CourseRegistered.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section)
			if Weightage<0:
				Weightage=0.0
			ObtainedMarks=request.POST.getlist('ObtainedMarks')
			for i in range(len(ObtainedMarks)):
				Evaluation.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section,StudentID=Students[i].StudentID,EvaluationNumber=EvalNum).update(Weightage=Weightage,TotalMarks=TotalMarks,ObtainedMarks=float(ObtainedMarks[i]),Type=Type)
			return HttpResponseRedirect(reverse('TeacherDashboard'))

		else:
			return HttpResponseRedirect(reverse('TeacherDashboard'))
	else:
		return HttpResponseRedirect(reverse('TeacherLogin'))
def TeacherEvaluationModInsertSave(request):
	if request.session.has_key('EmpID'):
		if request.method=='POST':
			form=request.POST
			Sem= Semester.objects.get(SemesterID=form.get('Sem'))
			batch=Batch.objects.get(BatchID=form.get('Batch'))
			course=Course.objects.get(CourseID=form.get('Course'))
			Section=form.get('Section')
			EvalNum=int(form.get('EvalNum'))
			Weightage=float(form.get('Weightage'))
			TotalMarks=float(form.get('TotalMarks'))
			Students=CourseRegistered.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section)
			if Weightage<0:
				Weightage=0.0
			ObtainedMarks=request.POST.getlist('ObtainedMarks')
			for i in range(len(ObtainedMarks)):
				Evaluation.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section,StudentID=Students[i].StudentID,EvaluationNumber=EvalNum).update(Weightage=Weightage,TotalMarks=TotalMarks,ObtainedMarks=float(ObtainedMarks[i]))
			return HttpResponseRedirect(reverse('TeacherDashboard'))

		else:
			return HttpResponseRedirect(reverse('TeacherDashboard'))
	else:
		return HttpResponseRedirect(reverse('TeacherLogin'))

def TeacherAttendanceMod(request):
	if request.session.has_key('EmpID'):
		if request.method=='POST':
			form=request.POST
			SemID= Semester.objects.order_by('Start_Date').reverse()[0].SemesterID
			Batch=form.get('Batch')
			Course=form.get('Course')
			SectionID=form.get('Section')
			Data=Attendance.objects.filter(SemesterID=SemID,BatchID=Batch,CourseID=Course,Section=SectionID).order_by('StudentID')
			if len(Data)>0:
				StudentIDs=[]
				Present=[]
				TotalCount=[]
				Dates=[]
				for i in Data:
					if i.StudentID not in StudentIDs:
						StudentIDs.append(i.StudentID)
						Present.append(0.0)
						TotalCount.append(0.0)
					if i.LectureNo>1 :
						Index=StudentIDs.index(i.StudentID)
						TotalCount[Index]+=(1*i.Duration)
						if i.Presence=='Present' or i.Presence=='Not Registered':
							Present[Index]+=i.Duration
						if i.Date not in Dates:
							Dates.append(i.Date)
				for i in range(len(StudentIDs)):
					if TotalCount[i]==0:
						Present[i]=100
					else:
						Present[i]*=100
						Present[i]/=TotalCount[i]
				Names=Student.objects.filter(pk__in=StudentIDs)
				Context={
					'Records':zip(StudentIDs,Names,Present),
					'Sem':SemID,
					'Batch':Batch,
					'Course': Course,
					'Section': SectionID,
					'Dates':Dates
				}
				return render(request,'AMS/ViewAttendance.html',Context)
			else:
				return HttpResponseRedirect(reverse('TeacherAttendance'))
		else:
			return HttpResponseRedirect(reverse('TeacherAttendance'))
	else:
		return HttpResponseRedirect(reverse('TeacherLogin'))

def TeacherEvaluationMod(request):
	if request.session.has_key('EmpID'):
		if request.method=='POST':
			form=request.POST
			SemID= Semester.objects.order_by('Start_Date').reverse()[0].SemesterID
			Batch=form.get('Batch')
			Course=form.get('Course')
			SectionID=form.get('Section')
			Data=Evaluation.objects.filter(SemesterID=SemID,BatchID=Batch,CourseID=Course,Section=SectionID).order_by('StudentID')
			if len(Data)>0:
				StudentIDs=[]
				Marks=[]
				TotalMarks=0.0
				EvalNumber=[]
				for i in Data:
					if i.StudentID not in StudentIDs:
						StudentIDs.append(i.StudentID)
						Marks.append(0.0)
					if i.EvaluationNumber not in EvalNumber:
						EvalNumber.append(i.EvaluationNumber)
						TotalMarks+=i.Weightage
					Index=StudentIDs.index(i.StudentID)

					
					if i.TotalMarks!=0:
						Marks[Index]+=(i.Weightage*(i.ObtainedMarks/i.TotalMarks))
				if TotalMarks<=0.0:
					for i in range(len(Marks)):
						Marks[i]=100
				else:
					Marks[:] = [((x*100)/TotalMarks) for x in Marks]
				EvalNumber.remove(min(EvalNumber))
				Names=Student.objects.filter(pk__in=StudentIDs)
				Types=['Assignment','Quiz','Mid Exam','Lab Task','Final Exam']
				Gradings=['Absolute']
				Context={
					'Records':zip(StudentIDs,Names,Marks),
					'Sem':SemID,
					'Batch':Batch,
					'Course': Course,
					'Section': SectionID,
					'TotalMarks':TotalMarks,
					'Types':Types,
					'Evals':EvalNumber,
					'Gradings':Gradings
				}
				return render(request,'AMS/ViewEvaluation.html',Context)
			else:
				return HttpResponseRedirect(reverse('TeacherEvaluation'))
		else:
			return HttpResponseRedirect(reverse('TeacherAttendance'))
	else:
		return HttpResponseRedirect(reverse('TeacherLogin'))
def getGrade(Score):
	if Score>95:
		return 'A+'
	elif Score>90:
		return 'A'
	elif Score>85:
		return 'A-'
	elif Score>80:
		return 'B+'
	elif Score>75:
		return 'B'
	elif Score>70:
		return 'B-'
	elif Score>65:
		return 'C+'
	elif Score>60:
		return 'C'
	elif Score>55:
		return 'C-'
	elif Score>50:
		return 'D+'
	elif Score>=40:
		return 'D'
	else :
		return 'F'

def TeacherGrading(request):
	if request.session.has_key('EmpID'):
		if request.method=='POST':
			form=request.POST
			SemID= Semester.objects.order_by('Start_Date').reverse()[0].SemesterID
			Batch=form.get('Batch')
			Course=form.get('Course')
			Section=form.get('Section')
			GradingScheme=form.get('GradingScheme')
			Records=CourseRegistered.objects.filter(SemesterID=SemID,BatchID=Batch,CourseID=Course,Section=Section)
			Evaluations=Evaluation.objects.filter(SemesterID=SemID,BatchID=Batch,CourseID=Course,Section=Section).order_by('SemesterID','BatchID','CourseID','Section','StudentID')
			ScoresObtained=[]
			TotalWeightage=[]
			Students=[]
			for i in range(len(Evaluations)):
				if Evaluations[i].StudentID not in Students:
					Students.append(Evaluations[i].StudentID)
					ScoresObtained.append(0)
					TotalWeightage.append(0)
				Index=Students.index(Evaluations[i].StudentID)
				if Evaluations[i].EvaluationNumber>1:
					ScoresObtained[Index]+=(Evaluations[i].Weightage*(Evaluations[i].ObtainedMarks/Evaluations[i].TotalMarks))
					TotalWeightage[Index]+=Evaluations[i].Weightage
			print('\n\n')
			for i in range(len(ScoresObtained)):
				ScoresObtained[i]*=100
				ScoresObtained[i]/=TotalWeightage[i]
				print(ScoresObtained[i])
				CourseRegistered.objects.filter(SemesterID=SemID,BatchID=Batch,CourseID=Course,Section=Section,StudentID=Students[i]).update(Grade=getGrade(ScoresObtained[i]))
		return HttpResponseRedirect(reverse('TeacherDashboard'))
	else:
		return HttpResponseRedirect(reverse('TeacherLogin'))
def TeacherAttendanceModUpdateSave(request):
	if request.session.has_key('EmpID'):
		if request.method=='POST':
			form=request.POST
			Sem= Semester.objects.get(SemesterID=form.get('Sem'))
			batch=Batch.objects.get(BatchID=form.get('Batch'))
			course=Course.objects.get(CourseID=form.get('Course'))
			Section=form.get('Section')
			Students=CourseRegistered.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section)
			Lecture=Attendance.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course, Section=Section, Date=form.get('Date'))[0].LectureNo
			Duration=float(form.get('Duration'))

			if Duration<0:
				Duration=0.0
			Attendances=request.POST.getlist('Attendance')
			for i in range(len(Attendances)):
				Attendance.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section,StudentID=Students[i].StudentID,LectureNo=Lecture).update(Duration=Duration,Presence=Attendances[i])
			return HttpResponseRedirect(reverse('TeacherDashboard'))

		else:
			return HttpResponseRedirect(reverse('TeacherDashboard'))
	else:
		return HttpResponseRedirect(reverse('TeacherLogin'))
def TeacherAttendanceModInsertSave(request):
	if request.session.has_key('EmpID'):
		if request.method=='POST':
			form=request.POST
			Sem= Semester.objects.get(SemesterID=form.get('Sem'))
			batch=Batch.objects.get(BatchID=form.get('Batch'))
			course=Course.objects.get(CourseID=form.get('Course'))
			Section=form.get('Section')
			Students=CourseRegistered.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section)
			Lecture=Attendance.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course, Section=Section, Date=form.get('Date'))[0].LectureNo
			Duration=float(form.get('Duration'))
			if Duration<0:
				Duration=0.0
			Attendances=request.POST.getlist('Attendance')
			for i in range(len(Attendances)):
				Attendance.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section,StudentID=Students[i].StudentID,LectureNo=Lecture).update(Duration=Duration,Presence=Attendances[i])
			return HttpResponseRedirect(reverse('TeacherDashboard'))

		else:
			return HttpResponseRedirect(reverse('TeacherDashboard'))
	else:
		return HttpResponseRedirect(reverse('TeacherLogin'))
def TeacherAttendanceModUpdate(request):
	if request.session.has_key('EmpID'):
		if request.method=='POST':
			form=request.POST
			Sem= Semester.objects.get(SemesterID=form.get('Sem'))
			batch=Batch.objects.get(BatchID=form.get('Batch'))
			course=Course.objects.get(CourseID=form.get('Course'))
			Section=form.get('Section')
			Date=form.get('Date')
			Data=Attendance.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section,Date=Date)
			Options=['Present','Absent','Not Registered']
			if Data:
				Students=CourseRegistered.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section)
				Names=[]
				StudentIDs=[]
				Present=[]
				for i in Data:
					Duration=i.Duration
					if i.StudentID not in StudentIDs:
						StudentIDs.append(i.StudentID)
						Present.append(i.Presence)
				Names=Student.objects.filter(pk__in=StudentIDs)
				Context={
					'Records':zip(StudentIDs,Names,Present),
					'Options':Options,
					'Semester':form.get('Sem'),
					'Batch':batch,
					'Course': course,
					'Section': Section,
					'Date':Date,
					'Duration':Duration

				}
				return render(request,'AMS/UpdateAttendance.html',Context)
			else:
				return HttpResponseRedirect(reverse('TeacherDashboard'))
		else:
			return 	HttpResponseRedirect(reverse('TeacherDashboard'))
	else:
		return HttpResponseRedirect(reverse('TeacherLogin'))	
def TeacherAttendanceModInsert(request):
	if request.session.has_key('EmpID'):
		if request.method=='POST':
			form=request.POST
			Sem= Semester.objects.get(SemesterID=form.get('Sem'))
			batch=Batch.objects.get(BatchID=form.get('Batch'))
			course=Course.objects.get(CourseID=form.get('Course'))
			Section=form.get('Section')
			Date=form.get('Date')

			Objects=Attendance.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section,Date=Date).order_by('LectureNo')
			if not Objects:
				Students=CourseRegistered.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section)
				Objects=Attendance.objects.filter(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section).order_by('LectureNo').reverse()
				Count=Objects[0].LectureNo
				for i in range(len(Students)):
					New=Attendance(SemesterID=Sem,BatchID=batch,CourseID=course,Section=Section,StudentID=Students[i].StudentID,LectureNo=Count+1,Date=Date,Duration=0,Presence='Absent')
					New.save()
				return TeacherAttendanceModUpdate(request)
			return HttpResponseRedirect(reverse('TeacherAttendance'))
		return HttpResponseRedirect(reverse('TeacherAttendance'))
