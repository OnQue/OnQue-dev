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
    name = models.CharField(null=True,blank=True,max_length=32)
    age = models.IntegerField(blank=False,max_length=2)
    conversion = models.BooleanField(default=False)
    bill = models.IntegerField(blank=True,max_length=10,null=True)
    table_num = models.CharField(default='0',max_length =32)  #Table no in which he is seated
    waiting = models.BooleanField(default=True)
    seated = models.BooleanField(default=False)
    directly_seated = models.BooleanField(default=False)
    take_away = models.BooleanField(default=False)
    no_show = models.BooleanField(default=False)

class Feedback(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True, blank=False)
    mobile = models.IntegerField(blank=False,max_length=10)
    service = models.IntegerField(blank=True,null=True)
    ambience = models.IntegerField(blank=True,null=True)
    Food = models.IntegerField(blank=True,null=True)
    record = models.ForeignKey(Record,null=True)










