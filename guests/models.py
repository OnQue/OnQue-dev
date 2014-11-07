from django.db import models

# Create your models here.
from django.db import models
from jsonfield import JSONField

# Create your models here.
class Guest(models.Model):
    mobile = models.IntegerField(max_length=10, primary_key=True)
    name = models.CharField(blank=True, max_length =32)
    age = models.IntegerField(blank=True,default=18)
    created_at = models.DateTimeField(blank=False)
    restuarants = JSONField(default={'visited':[]})
    last_visited = JSONField(default={'restuarant':'','date':''})
    start_time = models.DateTimeField(blank=True,null=True)
    waiting_time = models.IntegerField(blank=True,max_length=2,default=0)
    status = models.IntegerField(default=0)   #0-nothing 1-waitinglist 2-seated
    table_no = models.IntegerField(default=0)  #Table no in which he is seated
    current = models.CharField(default="null", max_length =32)  #Rest at which currently seated or waiting list
