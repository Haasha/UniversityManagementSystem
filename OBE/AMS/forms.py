from AMS.models import *
from django.forms import ModelForm

class CourseRegistrationsForm(ModelForm):
	class Meta:
		model=CourseRegistration
		fields=['Section','Box']

