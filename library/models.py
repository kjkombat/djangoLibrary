from django.db import models

class Books(models.Model):
	author = models.CharField(max_length=200)
	book_name = models.CharField(max_length=200)
	
	LOAN_STATUS = (
	('a','Avaiable'),
	('r','Reserved'),
	)
	
	status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a', help_text= 'Availability')
	def __str__(self):
		return self.book_name
	


class students(models.Model):
	student_name = models.CharField(max_length=200)
	book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
	def __str__(self):
		return self.student_name
	
	#def __str__(self):
	#	return self.student_name
# Create your models here.
