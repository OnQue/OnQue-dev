from django.db import models

# Create your models here.
from django.db import models
from jsonfield import JSONField

# Create your models here.
class Guest(models.Model):
    mobile = models.IntegerField(max_length=10, primary_key=True)
    name = models.CharField(blank=True, max_length =32)
    age = models.IntegerField(blank=True)
    restuarants = JSONField(default={'visited':[]})
    last_visited = JSONField(default={'restuarant':'','date':''})
