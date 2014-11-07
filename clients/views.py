from django.shortcuts import render,render_to_response
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from clients.forms import MyForm, AdminSettingsForm, AddGuestForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from clients.models import table
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import json
from django.contrib.auth.models import User
from OnQueue import utils
from guests.models import Guest



_MSG_CODES = {'swg': 'Sorry Wrong credentials',
			  'slo': 'Successfully Logged out',
			  'rsl': 'Registered Successfully Please Log in now',
			  'lap': 'Please login to access that page'}


@receiver([post_save], sender=User)
def init_newuser_data(sender, **kwargs):
	'''
	Whenever a new user is created no of tables is assigned to 10
	with all tables as free
	'''
	user = kwargs.get('instance')
	try:
		t, t_created = table.objects.get_or_create(user=user,
            defaults={'user':user,'n_of_table':10,'status':{'free':[1,2,3,4,5,6,7,8,9,10],'booked':[]}})
	except MultipleObjectsReturned:
		pass


def api(request):
	response={"response":'An error occured'}
	if request.user.is_authenticated():
		t=table.objects.get(user=request.user)
		response=t.status
		# return HttpResponse(json.dumps(response), content_type="application/json")
	return HttpResponse(json.dumps(response), content_type="application/json") 

def get_waiting_list_of_table(request):
	response={"response":'An error occured'}
	if request.user.is_authenticated():
		t=table.objects.get(user=request.user)
		response=t.status
		# return HttpResponse(json.dumps(response), content_type="application/json")
	return HttpResponse(json.dumps(response), content_type="application/json") 





def login(request):
	if request.method == 'POST':
	    username = request.POST.get('username', '')
	    password = request.POST.get('password', '')
	    user = auth.authenticate(username=username, password=password)
	    if user is not None and user.is_active:
	        # Correct password, and the user is marked "active"
	        auth.login(request, user)
	        # Redirect to a success page.
	        return HttpResponseRedirect("/dashboard/")

	    else:
	        # Show an error page
	        return render(request,'clients/login.html',{'msg':_MSG_CODES['swg']})

	msg=request.GET.get('msg','')

	return render(request, 'clients/login.html',{'msg':msg})


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/login?msg=%s' %_MSG_CODES['slo'])
    # return render(request, 'clients/login.html', {'msg':_MSG_CODES['slo']})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/login?msg=%s' %_MSG_CODES['rsl'])
            # return render(request,'clients/login.html',{'msg':'Registered Successfully Please Log in now'})
    else:
        form = UserCreationForm()
    return render(request, "clients/register.html", {
        'form': form,
    })


def loggedin(request):
	if  request.user.is_authenticated():
		t = table.objects.get(user=request.user)
		return render(request,'clients/loggedin.html', {'n_of_tables':t.n_of_table,'status':t.status})
	else:
		# return HttpResponseRedirect('/login?msg=%s' %_MSG_CODES['lap'])
		return render(request,'clients/login.html',{'msg':'Please login to access that page'})


def process_status(request):
	post = request.POST.copy()
	no = post.get('checkout_table')
	booked = table.objects.get(user=request.user).status['booked']
	free = table.objects.get(user=request.user).status['free']
	booked.remove(int(no))
	free.append(int(no))
	booked.sort()
	free.sort()
	st={"booked":booked,"free":free}
	post['status']=st
	return post



def update_tables(request):
	if  request.user.is_authenticated():
		instance=table.objects.get(user=request.user)
		if request.method == "POST":
			post = process_status(request)
			form = MyForm(post, instance=instance)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/loggedin/')
		form = MyForm(None, instance=instance)
		return render(request, 'clients/old_templates/update_tables.html', {'form': form})
	else:
		return render(request,'clients/login.html',{'msg':'Please login to access that page'})

def update_default(request):
	if  request.user.is_authenticated():
		instance=table.objects.get(user=request.user)
		if request.method == "POST":
			form = MyForm(request.POST, instance=instance)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/loggedin/')
		form = MyForm(None, instance=instance)
		return render(request, 'clients/old_templates/update_tables.html', {'form': form})
	else:
		return render(request,'clients/login.html',{'msg':'Please login to access that page'})

def waitlist(request):
	if  request.user.is_authenticated():
		return render(request,'clients/waitlist.html')

	return HttpResponseRedirect('/login?msg=%s' %_MSG_CODES['lap'])

def checkout(request):
	if  request.user.is_authenticated():
		if request.method == 'POST':
			t_n = int(request.POST.get('checkout_table'))
			t=table.objects.get(user=request.user)
			free = t.status['free']
			booked = t.status['booked']
			booked.remove(int(t_n))
			free.append(int(t_n))
			booked.sort()
			free.sort()
			t.status={"booked":booked,"free":free}
			seated = t.seated['seated']
			
			for guest in seated:
				g=Guest.objects.get(mobile=guest)
				if g.table_no ==t_n:
					seated.remove(guest)
					g.current = "null"
					g.status = 0
					table_no = 0
					restuarant = request.user.username
					date = utils.time_now()
					g.last_visited ={'restuarant':restuarant,'date':date}
					visited = g.restuarants['visited']
					visited.append(restuarant)
					g.restuarants={'visited':visited}
					g.save(update_fields=['current','status','last_visited','restuarants']) 
			t.save(update_fields=['status','seated'])
			return HttpResponseRedirect('/')

		return render(request,'clients/checkout.html')

	return HttpResponseRedirect('/login?msg=%s' %_MSG_CODES['lap'])

def admin_settings(request):
	if  request.user.is_authenticated():
		if request.method == "POST":
			t=table.objects.get(user=request.user)
			n = int(request.POST.get('n_of_table'))
			t.n_of_table = n
			free = []
			for i in range(1,n+1): 
				free.append(i)
			free.sort()
			t.status = {'booked':[],'free':free}
			t.seated = {'seated':[]}
			t.waiting_list = {'waiting_list':[]}
			t.save(update_fields=['n_of_table','seated','waiting_list','status'])
			return HttpResponseRedirect('/')
		return render(request, 'clients/update_tables.html')
		
	return HttpResponseRedirect('/login?msg=%s' %_MSG_CODES['lap'])



def dashboard(request):
	if  request.user.is_authenticated():
		n_of_tables = table.objects.get(user=request.user)
		seated=utils.get_seated_guests(request.user)
		waiting=utils.get_waiting_guests(request.user)

		return render(request,'clients/dashboard.html', {'n_of_tables':n_of_tables.n_of_table,'status':n_of_tables.status,'seated':seated,'waiting':waiting})
	else:
		return HttpResponseRedirect('/login?msg=%s' %_MSG_CODES['lap'])
		

def add(request):
	errors = []
	if  request.user.is_authenticated():
		if request.method == 'POST':
			mobile = int(request.POST.get('mobile', ''))
			errors = []
			print mobile,"-------------------------------"
			waiting_list = utils.get_waiting_guests(request.user)
			if not mobile in waiting_list:  #Check if he's not already in waiting list
				if utils.guest_exists(mobile):
					g = Guest.objects.get(mobile=mobile)
					g.waiting_time = 5
					g.start_time = utils.time_now()
					g.status = 1  #Waiting list
					g.current = request.user.username
					g.save(update_fields=['waiting_time','start_time','status','current'])
				else:
					g=Guest(mobile=mobile,created_at=utils.time_now(),status=1,current = request.user.username,waiting_time = 5)
					g.save()
					utils.send_link_to_register(mobile)
				##Add user to the waiting list
				u=User.objects.get(username=request.user.username)
				utils.update_waiting_list(u,g)
			else:
				errors.append("%d already  in waiting list" %mobile)
			print errors,"========ERROR================"
		form = AddGuestForm()
		waiting = utils.get_waiting_detail(request.user)

		return render(request, 'clients/add.html', {'form':form,'waiting':waiting,'errors':errors})
	else:
		return HttpResponseRedirect('/login?msg=%s' %_MSG_CODES['lap'])

def countdown(request):
	time = 30
	return render(request,'clients/countdown.html',{'time':time})

def seated(request):
	if  request.user.is_authenticated():
		if request.method == 'POST':
			guest_num = int(request.POST.get('guest_num'))
			table_num = int(request.POST.get('table_num'))
			t=table.objects.get(user=request.user)
			free = t.status['free']
			booked = t.status['booked']
			booked.append(int(table_num))
			print table_num,"----------------------------------------"
			free.remove(int(table_num))
			booked.sort()
			free.sort()
			seated = t.seated['seated']
			waiting = t.waiting_list['waiting_list']
			seated.append(guest_num)
			waiting.remove(guest_num)
			t.seated = {'seated':seated}
			t.waiting_list = {'waiting_list':waiting}

			t.status={"booked":booked,"free":free}
			t.save(update_fields=['status','waiting_list','seated'])
			g=Guest.objects.get(mobile=guest_num)
			g.current=request.user.username
			g.table_no = table_num
			g.status = 2
			g.save(update_fields=['current','table_no','status'])
			return HttpResponseRedirect('/')

		return render(request,'clients/seated.html')

	return HttpResponseRedirect('/login?msg=%s' %_MSG_CODES['lap'])
	




