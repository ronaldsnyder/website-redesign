from django.db import models

# Create your models here.


class Education(models.Model):
    college = models.CharField(max_length=255)
    start = models.CharField(max_length=255)
    end = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    awards = models.CharField(max_length=255, blank = True, null=True)

#Everything related to work experience and job History
class Employer(models.Model):
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    
class Job(models.Model):
    employer = models.ForeignKey('Employer')
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

class Responsibility(models.Model):
    employer = models.ForeignKey('Job')
    description = models.TextField()
    
class Accomplishment(models.Model):
    employer = models.ForeignKey('Job')
    description = models.TextField()
    
class Tech(models.Model):
    type = models.CharField(max_length=255)

class HardSkill(models.Model):
    skill = models.ForeignKey('Tech')
    hard_skill = models.CharField(max_length=255) 
    
class SoftSkill(models.Model):
    technology = models.ForeignKey('Tech')
    soft_skill = models.CharField(max_length=255)     

    
    
    
    