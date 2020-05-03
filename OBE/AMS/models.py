from django.db import models
# Create your models here.

Gender=(('Male','Male'),('Female','Female'),('Other','Other'))
Positions=(('Lecturer','Lecturer'),('Associate Professor','Associate Professor'),('Assistant Professor','Assistant Professor'),('Professor','Professor'))
Grade_Choices=(('A+','A+'),('A','A'),('A-','A-'),('B+','B+'),('B','B'),('B-','B-'),('C+','C+'),('C','C'),('C-','C-'),('D+','D+'),('D','D'),('F','F'),('W','W'),('I','I'))
SemesterNumber=(('1','1st'),('2','2nd'),('3','3rd'),('4','4th'),('5','5th'),('6','6th'),('7','7th'),('8','8th'),)
CLO_Choices=(('Affective','Affective'),('Cognitive','Cognitive'),('Psychomotor','Psychomotor'))
Course_Choices=(('Core','Core'),('Elective','Elective'))
Status_Choices=(('Current','Current'),('Graduated','Graduated'))
Presence_Choices=(('Present','Present'),('Absent','Absent'),('Not Registered','Not Registered'))
Sections=(('A','A'),('B','B'),('C','C'),('D','D'),('E','E'),('F','F'),('G','G'),('H','H'),('I','I'),('J','J'),('K','K'),('L','L'),('M','M'),('N','N'),('O','O'),('P','P'),('Q','Q'),('R','R'),('S','S'),('T','T'),('U','U'),('V','V'),('W','W'),('X','X'),('Y','Y'),('Z','Z'))
Type_Choices=(('Assignment','Assignment'),('Quiz','Quiz'),('Mid Exam','Mid Exam'),('Lab Task','Lab Task'),('Final Exam','Final Exam'))
class Department(models.Model):
	DeptID=models.CharField(max_length=10,primary_key=True)
	Name=models.CharField(max_length=50)
	Desc=models.CharField(max_length=200, blank=True,null=True)
	def __str__(self):
		return self.DeptID

class Program(models.Model):
	ProgramID=models.CharField(max_length=10,primary_key=True)
	Name=models.CharField(max_length=100)
	DepartmentID=models.ForeignKey(Department,on_delete=models.CASCADE)
	MinSemesters=models.PositiveSmallIntegerField()
	MaxSemesters=models.PositiveSmallIntegerField()
	def __str__(self):
		return self.Name

class Course(models.Model):
	CourseID=models.CharField(max_length=6, primary_key=True)
	Title=models.CharField(max_length=100)
	Description=models.CharField(max_length=200, blank=True,null=True)
	CreditHours=models.PositiveSmallIntegerField()
	PreReq=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
	def __str__(self):
		return self.CourseID

class Semester(models.Model):
	SemesterID=models.CharField(max_length=10, primary_key=True)
	Name=models.CharField(max_length=20)
	Start_Date=models.DateField()
	End_Date=models.DateField()
	def __str__(self):
			return self.Name

class ProgramOutline(models.Model):
	ProgramID=models.ForeignKey(Program,on_delete=models.CASCADE)
	SemesterNumber=models.PositiveSmallIntegerField()
	CourseID=models.ForeignKey(Course,on_delete=models.CASCADE)
	CourseType=models.CharField(max_length=20,choices=Course_Choices)
	Description=models.CharField(max_length=100,null=True,blank=True)
	class Meta:
			unique_together=['ProgramID','SemesterNumber','CourseID']
	def __str__(self):
		return str(self.ProgramID) + '_'+ str(self.SemesterNumber) + '_'+ str(self.CourseID)

class Batch(models.Model):
	BatchID=models.CharField(max_length=20,primary_key=True)
	Name=models.CharField(max_length=100)
	Recruitment_Date=models.DateField(null=True,blank=True)
	def __str__(self):
		return self.BatchID

class Student(models.Model):
	StudentID=models.CharField(max_length=10,primary_key=True)
	Name=models.CharField(max_length=100)
	Email=models.EmailField()
	DoB=models.DateField(null=True,blank=True)
	CNIC=models.CharField(max_length=13,null=True,blank=True)
	Password=models.CharField(max_length=200)
	Gender=models.CharField(max_length=10,null=True,blank=True,choices=Gender)
	PhoneNo=models.CharField(max_length=11, null=True, blank=True)
	ProgramID=models.ForeignKey(Program,on_delete=models.CASCADE)
	BatchID=models.ForeignKey(Batch,on_delete=models.CASCADE)
	Section=models.CharField(max_length=1,choices=Sections, null=True, blank=True)
	Status=models.CharField(max_length=20,choices=Status_Choices,null=True,blank=True)

	PermanentAddress=models.CharField(max_length=200,blank=True,null=True)
	PermanentPhone=models.CharField(max_length=11, null=True, blank=True)
	PermanentPostalCode=models.CharField(max_length=5,blank=True,null=True)
	PermanentCity=models.CharField(max_length=50,blank=True,null=True)
	TemporaryAddress=models.CharField(max_length=200,blank=True,null=True)
	TemporaryPhone=models.CharField(max_length=11, null=True, blank=True)
	TemporaryPostalCode=models.CharField(max_length=5,blank=True,null=True)
	TemporaryCity=models.CharField(max_length=50,blank=True,null=True)
	def __str__(self):
		return self.StudentID

class Employee(models.Model):
	EmployeeID=models.CharField(max_length=10,primary_key=True)
	Name=models.CharField(max_length=100)
	Email=models.EmailField()
	CNIC=models.CharField(max_length=13,null=True,blank=True)
	DOB=models.CharField(max_length=13,null=True,blank=True)
	Designation=models.CharField(max_length=20,null=True, blank=True,choices=Positions)
	Password=models.CharField(max_length=200)
	Gender=models.CharField(max_length=10,null=True,blank=True, choices=Gender)
	PhoneNo=models.CharField(max_length=11, null=True, blank=True)
	HireDate=models.DateField()
	Salary=models.IntegerField()
	DeptID=models.ForeignKey(Department,on_delete=models.CASCADE)

	PermanentAddress=models.CharField(max_length=200,blank=True,null=True)
	PermanentPhone=models.CharField(max_length=11, null=True, blank=True)
	PermanentPostalCode=models.CharField(max_length=5,blank=True,null=True)
	PermanentCity=models.CharField(max_length=50,blank=True,null=True)
	TemporaryAddress=models.CharField(max_length=200,blank=True,null=True)
	TemporaryPhone=models.CharField(max_length=11, null=True, blank=True)
	TemporaryPostalCode=models.CharField(max_length=5,blank=True,null=True)
	TemporaryCity=models.CharField(max_length=50,blank=True,null=True)
	def __str__(self):
		return str(self.Designation)+'.'+str(self.Name)

class CourseRegistration(models.Model):
	SemesterID=models.ForeignKey(Semester,on_delete=models.CASCADE)
	BatchID=models.ForeignKey(Batch,on_delete=models.CASCADE)
	CourseID=models.ForeignKey(Course,on_delete=models.CASCADE)
	Section=models.CharField(max_length=1,choices=Sections)
	EmployeeID=models.ForeignKey(Employee,on_delete=models.CASCADE)
	CourseType=models.CharField(max_length=20,choices=Course_Choices,null=True)
	SeatsLeft=models.PositiveIntegerField()
	Description=models.CharField(max_length=100)
	class Meta:
			unique_together=['SemesterID','BatchID','CourseID','Section']
	def __str__(self):
		return str(self.SemesterID) + '_'+ str(self.BatchID) + '_'+ str(self.CourseID) + '_' + str(self.Section)

class CourseRegistered(models.Model):
	SemesterID=models.ForeignKey(Semester,on_delete=models.CASCADE)
	BatchID=models.ForeignKey(Batch,on_delete=models.CASCADE)
	CourseID=models.ForeignKey(Course,on_delete=models.CASCADE)
	Section=models.CharField(max_length=1,choices=Sections,null=True)
	StudentID=models.ForeignKey(Student,on_delete=models.CASCADE)
	Grade=models.CharField(max_length=4,choices=Grade_Choices)
	class Meta:
		unique_together=['SemesterID','BatchID','CourseID','Section','StudentID']
	def __str__(self):
		return str(self.SemesterID) + '_'+ str(self.BatchID) + '_'+ str(self.CourseID) + '_'+ str(self.Section)+'_'+ str(self.StudentID)

class Evaluation(models.Model):
	SemesterID=models.ForeignKey(Semester,on_delete=models.CASCADE)
	BatchID=models.ForeignKey(Batch,on_delete=models.CASCADE)
	CourseID=models.ForeignKey(Course,on_delete=models.CASCADE)
	Section=models.CharField(max_length=1,choices=Sections,null=True)
	StudentID=models.ForeignKey(Student,on_delete=models.CASCADE)
	EvaluationNumber=models.PositiveIntegerField()
	Weightage=models.FloatField()
	TotalMarks=models.FloatField()
	ObtainedMarks=models.FloatField()
	Type=models.CharField(max_length=20,choices=Type_Choices,null=False)
	class Meta:
		unique_together=['SemesterID','BatchID','CourseID','Section','StudentID','EvaluationNumber']

class Attendance(models.Model):
	SemesterID=models.ForeignKey(Semester,on_delete=models.CASCADE)
	BatchID=models.ForeignKey(Batch,on_delete=models.CASCADE)
	CourseID=models.ForeignKey(Course,on_delete=models.CASCADE)
	Section=models.CharField(max_length=1,choices=Sections,null=True)
	StudentID=models.ForeignKey(Student,on_delete=models.CASCADE)
	LectureNo=models.PositiveIntegerField()
	Date=models.DateField(null=True, blank=True)
	Duration=models.FloatField(null=True,blank=True)
	Presence=models.CharField(max_length=20,choices=Presence_Choices,null=False)
	class Meta:
		unique_together=['SemesterID','BatchID','CourseID','Section','StudentID','LectureNo']

"""class Evaluations(models.Model):
	SemesterID=models.ForeignKey(Semester)
#class Attendance(models.Model):


#class Evaluations(models.Model):


class Campus(models.Model):
	CampusID=models.CharField(max_length=10,primary_key=True)
	Address=models.CharField(max_length=100)
	City=models.CharField(max_length=20)
	PhoneNo=models.CharField(max_length=20)
	def __str__(self):
		return self.CampusID

class Department(models.Model):
	DeptID=models.CharField(max_length=10,primary_key=True)
	Name=models.CharField(max_length=50)
	Desc=models.CharField(max_length=200, blank=True,null=True)
	#HeadOfDept=models.ForeignKey(Employee,blank=True,null=True)
	CampusID=models.ForeignKey(Campus, on_delete=models.CASCADE)
	def __str__(self):
		return self.DeptID

class DegreeType(models.Model):
	DegreeID=models.CharField(max_length=15,primary_key=True)
	Name=models.CharField(max_length=50)
	MinSemesters=models.PositiveSmallIntegerField()
	MaxSemesters=models.PositiveSmallIntegerField()
	def __str__(self):
		return self.DegreeID

class Program(models.Model):
	ProgramID=models.CharField(max_length=10,primary_key=True)
	Name=models.CharField(max_length=100)
	DegreeID=models.ForeignKey(DegreeType,on_delete=models.CASCADE)
	DepartmentID=models.ForeignKey(Department,on_delete=models.CASCADE)
	def __str__(self):
		return self.Name

class Course(models.Model):
	CourseID=models.CharField(max_length=6, primary_key=True)
	Title=models.CharField(max_length=100)
	Description=models.CharField(max_length=200, blank=True,null=True)
	CreditHours=models.PositiveSmallIntegerField()
	PreReq=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
	def __str__(self):
		return self.Title

class Semester(models.Model):
	SemesterID=models.CharField(max_length=10, primary_key=True)
	Name=models.CharField(max_length=20)
	Start_Date=models.DateField()
	End_Date=models.DateField()
	def __str__(self):
			return self.Name



class PEO_Version(models.Model):
	PEO_VersionID=models.AutoField(primary_key=True)
	UserID=models.CharField(max_length=50)
	Date=models.DateTimeField()
	Description=models.CharField(max_length=200)
	def __int__(self):
		return self.PEO_VersionID

class PEO(models.Model):
	PEO_VersionID=models.ForeignKey(PEO_Version,on_delete=models.CASCADE)
	PEO_ID=models.CharField(max_length=10)
	Description=models.CharField(max_length=200)
	
	class Meta:
		unique_together=(('PEO_VersionID','PEO_ID'),)
	def __str__(self):
		return self.PEO_ID

class PLO(models.Model):
	PLO_ID=models.CharField(max_length=6)
	Details=models.ForeignKey(PEO,on_delete=models.CASCADE)
	PLO_Title=models.CharField(max_length=20)
	PLO_Desc=models.CharField(max_length=200, blank=True, null=True)
	class Meta:
		unique_together=(('PLO_ID','Details'),)
	def __str__(self):
		return self.PLO_ID

class CLO(models.Model):
	CLO_ID=models.CharField(max_length=6, primary_key=True)
	CLO_Desc=models.CharField(max_length=200, blank=True, null=True)
	PLO_ID=models.ForeignKey(PLO,on_delete=models.CASCADE)
	CLO_Category=models.CharField(max_length=50,choices=CLO_Choices)
	def __str__(self):
		return self.CLO_ID

class ProgramOutline_Version(models.Model):
	ProgramOutline_VersionID=models.AutoField(primary_key=True)
	UserID=models.CharField(max_length=50)
	Date=models.DateTimeField()
	Description=models.CharField(max_length=200)
	def __str__(self):
		return self.ProgramOutline_VersionID

class ProgramOutline(models.Model):
	ProgramOutline_VersionID=models.ForeignKey(ProgramOutline_Version,on_delete=models.CASCADE)
	PEO_VersionID=models.ForeignKey(PEO_Version,on_delete=models.CASCADE)
	ProgramID=models.ForeignKey(Program,on_delete=models.CASCADE)
	SemesterNumber=models.PositiveSmallIntegerField()
	CourseID=models.ForeignKey(Course,on_delete=models.CASCADE)
	CLO_ID=models.ForeignKey(CLO,on_delete=models.CASCADE)
	CourseType=models.CharField(max_length=20,choices=Course_Choices)
	class Meta:
			unique_together=(('ProgramOutline_VersionID','PEO_VersionID','ProgramID','SemesterNumber','CourseID','CLO_ID'),)

class Batch(models.Model):
	BatchID=models.CharField(max_length=20,primary_key=True)
	Name=models.CharField(max_length=100)
	ProgOutlineVersion=models.ForeignKey(ProgramOutline_Version, on_delete=models.CASCADE)
	Recruitment_Date=models.DateTimeField()
	def __str__(self):
		return self.BatchID

class Student(models.Model):
	StudentID=models.CharField(max_length=10,primary_key=True)
	Name=models.CharField(max_length=100)
	Email=models.EmailField()
	Password=models.CharField(max_length=200)
	Gender=models.CharField(max_length=10,null=True,blank=True,choices=Gender)
	PhoneNo=models.CharField(max_length=11, null=True, blank=True)
	ProgramID=models.ForeignKey(Program,on_delete=models.CASCADE)
	BatchID=models.ForeignKey(Batch,on_delete=models.CASCADE)
	Section=models.CharField(max_length=2)
	def __str__(self):
		return self.StudentID

class Employee(models.Model):
	EmployeeID=models.CharField(max_length=10,primary_key=True)
	Name=models.CharField(max_length=100)
	Email=models.EmailField()
	Designation=models.CharField(max_length=20,null=True, blank=True,choices=Positions)
	Password=models.CharField(max_length=200)
	Gender=models.CharField(max_length=10,null=True,blank=True, choices=Gender)
	PhoneNo=models.CharField(max_length=11, null=True, blank=True)
	HireDate=models.DateField()
	Salary=models.IntegerField()
	DeptID=models.ForeignKey(Department,on_delete=models.CASCADE)
	def __str__(self):
		return self.EmployeeID
"""



