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
		return render(request,'clients/checkout.html')

	return HttpResponseRedirect('/login?msg=%s' %_MSG_CODES['lap'])

def admin_settings(request):
	if  request.user.is_authenticated():
		instance=table.objects.get(user=request.user)
		if request.method == "POST":
			post = process_admin_settings(request)
			form = AdminSettingsForm(post, instance=instance)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/loggedin/')
			else:
				#Form is not valid
				print "INVALID",form.errors
				return render(request, 'clients/update_tables.html', {'form': form})
		form = AdminSettingsForm(None, instance=instance)
		return render(request, 'clients/update_tables.html', {'form': form})
	else:
		return HttpResponseRedirect('/login?msg=%s' %_MSG_CODES['lap'])

def process_admin_settings(request):
	post = request.POST.copy()
	n = int(post.get('n_of_table'))
	free = []
	booked = []
	for i in range(1,n+1): 
		free.append(i)
	booked.sort()
	free.sort()
	st={"booked":booked,"free":free}
	post['status']=st
	return post

def dashboard(request):
	if  request.user.is_authenticated():
		n_of_tables = table.objects.get(user=request.user)
		return render(request,'clients/dashboard.html', {'n_of_tables':n_of_tables.n_of_table,'status':n_of_tables.status})
	else:
		return HttpResponseRedirect('/login?msg=%s' %_MSG_CODES['lap'])
		

def add(request):
	if  request.user.is_authenticated():
		form = AddGuestForm()
		return render(request, 'clients/add.html', {'form':form})
	else:
		return HttpResponseRedirect('/login?msg=%s' %_MSG_CODES['lap'])




