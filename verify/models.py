from django.db import models
from users.models import CustomUser
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    promo = models.CharField(max_length=250)
    code = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.user.username

class Course(models.Model):
    name = models.CharField(max_length=100)
    cote_max = models.IntegerField(default=20)
    def __str__(self):
        return self.name


class Cotes(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    cote = models.IntegerField(default=0)
   
   
    def __str__(self):
        return self.student.user.username



