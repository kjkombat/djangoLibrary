from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Books,students
from .forms import borrowform

def index(request):
	students_query = students.objects.all()
	books_query = Books.objects.all()
	return render(request, "library/index.html", {"students_query":students_query, "books_query":books_query})
	
def borrow(request):
	students_query = students.objects.all()
	books_query = Books.objects.all()
	
	form = borrowform(request.POST or None)
	if form.is_valid():
		students = form.save(commit=False)
		student.save()
		error = "success"
		form = borrowform()
		return render(request, "library/index.html", {"form":form, "students_query":students_query, "books_query":books_query, "error": error})
	form = borrowform()
	error = "Error"
	return render(request, "library/index.html", {"form":form, "students_query":students_query, "books_query":books_query, "error": error})

# Create your views here.
