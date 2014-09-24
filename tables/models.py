from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
# from django.db.models import CharField
from jsonfield import JSONField

# Create your models here.


class table(models.Model):
	user = models.ForeignKey(User)
	n_of_table = models.IntegerField(default=0)
	status = JSONField()
	



