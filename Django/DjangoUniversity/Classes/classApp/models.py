from django.db import models

# Create your models here.

# new class with assigned attributes
class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, default="", blank=True, null=False) 
    Course_Number = models.IntegerField(default="", blank=True, null=False)
    Instructor_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Duration = models.FloatField(default="", blank=True, null=False)
    
    
    object = models.Manager() # allows you to manage the objects in the model. 
    
    def __str__(self):
        return self.Title