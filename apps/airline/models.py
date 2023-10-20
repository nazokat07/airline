from django.db import models
from apps.plane.models import Plane

class Airline(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateField()
    planes = models.ForeignKey(Plane, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


'''class Project(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True, default='des')
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    members = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.title}'
    

class Task(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    deadline_date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField()

    def __str__(self):
        return f'{self.title}'''
    
