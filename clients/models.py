from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from jsonfield import JSONField
from django.core.validators import MaxValueValidator, MinValueValidator


class table(models.Model):
    user = models.ForeignKey(User,primary_key=True)
    rest_name = models.CharField(null=True,blank=True,max_length=32)
    n_of_table = models.IntegerField(default=0)
    status = JSONField()
    waiting_list = JSONField(default={'waiting_list':[]},null=True)
    seated = JSONField(default={'seated':[]},null=True)

    
class Record(models.Model):
    user = models.ForeignKey(User)
    rest_name = models.CharField(null=True,blank=True,max_length=32)
    date = models.DateTimeField(auto_now_add=True, blank=False)
    mobile = models.IntegerField(blank=False,max_length=10)
    age = models.IntegerField(blank=False,max_length=2)
    conversion = models.BooleanField(default=False)
    bill = models.IntegerField(blank=True,max_length=10,null=True)
    table_num = models.IntegerField(null=True,blank=True,max_length=10)
    waiting = models.BooleanField(default=True)
    seated = models.BooleanField(default=False)

class Feedback(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True, blank=False)
    mobile = models.IntegerField(blank=False,max_length=10)
    service = models.IntegerField(blank=True,null=True)
    ambience = models.IntegerField(blank=True,null=True)
    Food = models.IntegerField(blank=True,null=True)










