from django.db import models

# Create your models here.

TYPE_CHOICES = {
    ('Mr.', 'Mr.'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms'),
    ('Sir', 'Sir'),
    
}





class Profiles(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    First_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Last_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Email = models.CharField(max_length=60, default="", blank=True, null=False)
    Username = models.CharField(max_length=60, default="", blank=True, null=False)
    
    
    object = models.Manager()
    
    def __str__(self):
        return self.First_Name