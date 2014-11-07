# from django.db import models
# from django.contrib.auth.models import User

# class UserProfile(models.Model):
#     # This field is required.
#     user = models.OneToOneField(User)

#     # Other fields here
    
#     n_of_tables = models.IntegerField(max_length=20, default=0)

# # class SubUsers(models.Model):

# # class Tables(models.Model):
# # 	user = models.ForeignKey(User)
# # 	n = models.I
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
# from django.db.models import CharField
from jsonfield import JSONField

# Create your models here.


class table(models.Model):
    user = models.ForeignKey(User,primary_key=True)
    n_of_table = models.IntegerField(default=0)
    status = JSONField()
    waiting_list = JSONField(default={'waiting_list':[]},null=True)
    seated = JSONField(default={'seated':[]},null=True)
    # rest_name = models.CharField(editable=False,default=user.username)
    





