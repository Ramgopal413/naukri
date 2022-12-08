from django.contrib.auth.models import User
from django.db import models
from location_field.models.plain import PlainLocationField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
choices = (("M", "M"),
           ("F", "F"),
           ("N", "N"))


class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.TextField(default=True)
    date_of_start = models.DateField(default=True)
    description = models.CharField(max_length=40)


class Recruiter(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField()
    mobile = PhoneNumberField(blank=False)
    company = models.ForeignKey(Company, default=True, on_delete=models.SET_DEFAULT)
    designation = models.CharField(max_length=40)
    dob = models.DateField(max_length=30)


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=60)


class Job(models.Model):
    city = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    job_description = models.CharField(max_length=50)
    max_salary = models.FloatField()
    min_salary = models.FloatField()
    employment_type = models.CharField(max_length=40)
    max_experience = models.IntegerField(default=None)
    min_experience = models.IntegerField(default=None)
    company = models.ForeignKey(Company, default=True, on_delete=models.SET_DEFAULT)
    location = PlainLocationField(based_fields=['CITY'], zoom=7)
    industry_type = models.CharField(max_length=50)
    skills = models.ForeignKey(Skill, default=True, on_delete=models.SET_DEFAULT)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Applicant(models.Model):
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    dob = models.FloatField()
    gender = models.CharField(max_length=1, choices=choices, default=1)
    availablity = models.CharField(max_length=20)
    job = models.ForeignKey(Job, default=True, on_delete=models.SET_DEFAULT)
    recruiter = models.ManyToManyField(Recruiter)


class Experience(models.Model):
    project_name = models.CharField(max_length=60)
    project_description = models.CharField(max_length=70)
    from_to = models.DateField(default=None)
    company = models.ForeignKey(Company, default=True, on_delete=models.SET_DEFAULT)
    applicant = models.ManyToManyField(Applicant, blank=True)


class Qualification(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=70)
    from_to = models.DateField(default=None)
    applicant = models.ForeignKey(Applicant, default=True, on_delete=models.SET_DEFAULT)
