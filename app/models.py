from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    title = models.CharField(max_length=35)
    author = models.CharField(max_length=25)
    cover = models.ImageField(upload_to='book_covers')
    price = models.PositiveIntegerField()

class EmployeeDetails(models.Model):
    emp_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    emp_code = models.PositiveIntegerField()
    emp_name = models.CharField(max_length=50)
    emp_grade = models.IntegerField()
    emp_location = models.CharField(max_length=50)
    emp_project = models.CharField(max_length=50)
    emp_role = models.CharField(max_length=50)
    emp_status = models.CharField(max_length=50)
    emp_DOJ = models.DateField()


class ManagerDetails(models.Model):
    mng_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    mng_code = models.PositiveIntegerField()
    mng_name = models.CharField(max_length=50)
    mng_grade = models.IntegerField()
    mng_location = models.CharField(max_length=50)
    mng_project = models.CharField(max_length=50)
    mng_role = models.CharField(max_length=50)
    mng_status = models.CharField(max_length=50)
    mng_DOJ = models.DateField()


