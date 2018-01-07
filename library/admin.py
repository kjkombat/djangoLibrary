from django.contrib import admin
from .models import Books
from .models import students

admin.site.register(Books)
admin.site.register(students)

# Register your models here.
