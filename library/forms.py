from django import forms
from .models import students

class borrowform(forms.ModelForm):
	
	class Meta:
		model = students
		fields = ['student_name', 'book_id']
	
	
	
	
	