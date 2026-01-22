from django.db import models

class Student(models.Model):
    Department_Choices = [
    ('CS', 'Computer Science '),
    ('IT', 'Information Technology'),
    ('EC', 'Electronics and Communication'),
    ('ME', 'Mechanical Engineering'),
    ('CE', 'Civil Engineering'),
    ('EE', 'Electrical Engineering'),
    ('BT', 'Biotechnology'),
    ('others', 'Others'),
]
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.IntegerField(max_length=15, unique=True)
    department = models.CharField(choices=Department_Choices)
    
    def __str__(self):
        return self.name
    