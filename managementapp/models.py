from django.db import models
from django.db.models.fields import DateTimeField
# from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class manage(models.Model):
    CAT=((1,'Normal'),(2,'Urgent'))
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task=models.CharField(max_length=120)
    priority=models.IntegerField(choices=CAT)
    projects=models.CharField(max_length=500)
    Assigneto=models.CharField(max_length=200)
    status=models.BooleanField(default=True)

class projectlist(models.Model):
    projects=models.CharField(max_length=500)
    clients=models.CharField(max_length=500)
    Duedate=models.DateField(blank=True, null=True,editable=False)

class addusers(models.Model):
     name=models.CharField(max_length=200,null=True)
     pimage=models.ImageField(upload_to="image",null=True)
     email=models.CharField(max_length=200,null=True)
     mobile=models.CharField(max_length=200)
     qualification=models.CharField(max_length=200,null=True)
     designation=models.CharField(max_length=200,null=True)

