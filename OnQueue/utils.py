from guests.models import Guest
from clients.models import table
import datetime
from math import floor, ceil
from twill.commands import *
from datetime import timedelta
import urllib2
import json
from django.conf import settings


def guest_exists(mobile):
    try:
        my_object = Guest.objects.get(mobile=mobile)
    except Guest.DoesNotExist:
        return False
    return True

def send_link_to_register(mobile,name):
    message = "Hello %s welcome to OnQue, please go through the following link to complete your profile #" %name
    send_sms(mobile,message)

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

def get_waiting_time(guest):
    start_time = guest.start_time
    print start_time,time_now()
    diff = (time_now() - start_time).total_seconds()
    rem = guest.waiting_time*60 - floor(diff)
    if(rem <=0):
        retVal = -1
    else:
        retVal = int(ceil(rem/60.0))
    return retVal


def send_sms(number,message):
    
    print "==============SEND SMS=================="
    print "Number: ",number
    print "Message: ",message
    print "========================================"
    number = int(number)
    message=message.replace(' ','%20')
    response = 17011
    if settings.SEND_SMS:
        url = "http://login.bulksms360.in:8080/sendsms/bulksms?username=exp1-onquee&password=123456&type=0&dlr=1&destination=%s&source=ONQUEE&message=%s" %(number,message)
        response = urllib2.urlopen(url)
        response = response.read().split('|')[0]
    return (response)

def previous_days(n):
    l=[]
    for i in range(0,n):
        l.append(datetime.date.today()-timedelta(days=i))
    return (l)

def clean_dict_JSON(mydict):
    for key in mydict.keys():
        if type(key) is not str:
            try:
              mydict[str(key)] = mydict[key]
            except:
              try:
                mydict[repr(key)] = mydict[key]
              except:
                pass
        del mydict[key]

    return mydict

def get_last_visited_details(guest):
    date = guest.last_visited['date'].strftime("%B %d, %Y")
    place = guest.last_visited['restuarant']
    return ({'date':date,'place':place})

def get_user_details(waiting_list):
    # print waiting_list,"=================="
    a= waiting_list
    i = 0
    num = a[a.find("[")+1:a.find("]")]
    l= num.split(',')
    print l
    users = []
    if len(l)>=1 and l[0]!='':
        for num in l:
            user = {}
            print str((num[2:-1])),"VIKAS"
            g=Guest.objects.get(mobile=num[2:-1])
            user['name'] = g.name
            user['mobile'] = g.mobile
            user['age'] = g.age
            user['time_left'] = get_waiting_time(g)
            user['waiting_time'] = g.waiting_time
            user['lastVisited']=g.last_visited
            user['tablesReqd'] = 1
            users.append(user)

    print users
    return users

def user_to_client(user):
    t=table.objects.get(user=user)
    return t




    








