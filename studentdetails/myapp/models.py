from django.db import models


# Create your models here.
class Course(models.Model):
    course=models.CharField(max_length=50)
    def __str__(self):
        return self.course


class Day(models.Model):
    day=models.CharField(max_length=20)

    def __str__(self):
        return self.day
    


class Syllabus(models.Model):
    syllabus=models.CharField(max_length=50)
    def __str__(self):
        return self.syllabus


class Course_syllabus(models.Model):
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Day=models.ForeignKey(Day,on_delete=models.CASCADE) 
    Syllabus=models.ManyToManyField(Syllabus,null=True,blank=True)
    percentage=models.IntegerField()




