from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# class BloodGroup(models.Model):
#     GROUP=(
#         ('O positive','O positive'),
#         ('O negative','O negative'),
#         ('A positive','A positive'),
#         ('A negative','A negative'),
#         ('B positive','B positive'),
#         ('B negative','B negative'),
#         ('AB positive','AB positive'),
#         ('AB negative','AB negative'),
#         ("Don't know", "Don't know")
#     )

#     bloodgroup=models.CharField(max_length=15, choices=GROUP)

class Donor(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])

    def __str__(self):
        return self.name



class Doctor(models.Model):
    name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(max_length=50, blank=False)
    phone=models.IntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)],blank=False)
    hospital=models.CharField(max_length=50,blank=False)
    specialization=models.CharField(max_length=50, blank=False, null=True)

    def __str__(self):
        return self.name
    
class Patient(models.Model):
    GENDER=(
        ('Male','Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )

    name=models.CharField(max_length=50, blank=False, default=None)
    email=models.EmailField(max_length=50, blank=False, default=None)
    phone = models.IntegerField(validators=[MinValueValidator(1000000000),MaxValueValidator(9999999999)], blank=False, default=None)
    age=models.PositiveIntegerField(blank=False, null=True, default=0)
    gender=models.CharField(max_length=6, choices=GENDER, blank=False, default=None)
    doctor=models.ForeignKey(Doctor, on_delete=models.PROTECT)
    drecommend=models.FileField(upload_to='drecommend/' ,max_length=50, blank=False, null=True)
    wredommend=models.FileField(upload_to='wrecommend', max_length=50, blank=False, null=True)
    fundamount=models.PositiveIntegerField(blank=False, null=True)
    bloodgroup=models.CharField(max_length=20, blank=False, default="Don't know")
    # bloodgroup=models.CharField(max_length=20, choices=GROUP, unique=True)
    # bloodgroup=models.ForeignKey(BloodGroup, null=True, on_delete=models.PROTECT)


    def __str__(self):
        return self.name