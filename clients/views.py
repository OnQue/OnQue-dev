from django.shortcuts import render,render_to_response
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from clients.forms import MyForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from tables.models import table
import json

_MSG_CODES = {'swg': 'Sorry Wrong credentials',
			  'slo': 'Successfully Logged out',
			  'rsl': 'Registered Successfully Please Log in now',
			  'lap': 'Please login to access that page'}


def api(request):
	response={"response":'An error occured'}
	if request.user.is_authenticated():
		print request.user
		print "REACHED"
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
	        return HttpResponseRedirect("/loggedin/")

	    else:
	        # Show an error page
	        return render(request,'clients/login.html',{'msg':_MSG_CODES['swg']})

	msg=request.GET.get('msg','')

	return render(request, 'clients/login.html',{'msg':msg})


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return render(request, 'clients/login.html', {'msg':_MSG_CODES['slo']})

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
		n_of_tables = table.objects.get(user=request.user)
		return render(request,'clients/loggedin.html', {'n_of_tables':n_of_tables.n_of_table,'status':n_of_tables.status})
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
		return render(request, 'clients/update_tables.html', {'form': form})
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




