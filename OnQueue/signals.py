from guests.models import Guest, PersonalRecord
from clients.models import table,Record
import datetime
from math import floor
from OnQueue.utils import time_now
from utils import send_sms


def save_waiting(user,mobile,waitingtime):
    print "Save_waiting"
    guest = Guest.objects.get(mobile=mobile)
    rest_name = table.objects.get(user=user).rest_name
    record = Record(user=user,rest_name=rest_name,date=time_now(),mobile=mobile,age=guest.age,name=guest.name)
    record.save()
    pr = PersonalRecord(guest=guest,restuarant=rest_name,date=time_now())
    pr.save() 
    message="Hello %s, You have been added to wait list at %s and your waiting time is %s mins" %(guest.name,rest_name,str(waitingtime))
    send_sms(mobile,message)


def save_seated(user,mobile,table_num):
    print "save_seated"
    record = Record.objects.get(user=user,mobile=mobile,waiting=True)
    record.conversion = True
    record.waiting= False
    record.seated = True
    record.table_num = table_num
    record.save(update_fields=['conversion','waiting','seated','table_num'])

def save_checkout(user,mobile,bill):
    print "save_checkout"
    record = Record.objects.get(user=user,mobile=mobile,seated=True)
    record.seated = False
    record.bill = bill
    record.save(update_fields=['seated','bill'])
    message="Thank you for visiting %s, we would really appreciate if you could fill out the feedback form" %(record.rest_name)
    send_sms(mobile,message)


