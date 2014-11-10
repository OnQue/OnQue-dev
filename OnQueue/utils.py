from guests.models import Guest
from clients.models import table
import datetime
from math import floor
from twill.commands import *


def guest_exists(mobile):
    try:
        my_object = Guest.objects.get(mobile=mobile)
    except Guest.DoesNotExist:
        return False
    return True

def send_link_to_register(mobile):
    print "Sent the link to register via sms to %s" %mobile

def time_now():
    return datetime.datetime.now()

def signal_add_waiting_list(u,g):
    pass

def update_waiting_list(u,g):
    t=table.objects.get(user=u)
    w=t.waiting_list['waiting_list']
    w.append(g.mobile)
    t.waiting_list = {'waiting_list':w}
    t.save(update_fields=['waiting_list'])

def update_seated(u,g):
    t=table.objects.get(user=u)
    s=t.seated['seated']
    s.append(g.mobile)
    t.seated = {'seated':s}
    t.save(update_fields=['seated'])

def get_seated_guests(u):
    t=table.objects.get(user=u)
    s=t.seated['seated']
    return s

def get_waiting_guests(u):
    t=table.objects.get(user=u)
    w=t.waiting_list['waiting_list']
    return w

def get_waiting_detail(u):
    retVal = {}
    mobiles = get_waiting_guests(u)
    for mobile in mobiles:
        guest=Guest.objects.get(mobile=mobile)
        start_time = guest.start_time
        print start_time,time_now()
        diff = (time_now() - start_time).total_seconds()
        rem = guest.waiting_time*60 - floor(diff)
        if(rem <=0):
            retVal[mobile]=-1
        else:
            retVal[mobile]=rem
    return retVal

def sendSMS(number,message):
        try:

                go("http://www.indyarocks.com")
                fv("1","LoginForm[username]",username)
                fv("1","LoginForm[password]",password)
                submit()
        except:
                print "Sorry this API needs updation, please report it under issues at https://github.com/mishravikas/pyIndyaSMS "
        

        try:
                go("http://www.indyarocks.com/send-free-sms")
                fv("3","FreeSms[mobile]",number)
                fv("3","FreeSms[post_message]",message)
                submit()
                print "Successfully sent"
        except:
                print "Username and password did not match"










