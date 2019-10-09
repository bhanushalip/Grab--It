from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render, reverse
from django.urls import resolve
from .decorators import find_worth
from .forms import SignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Item

# Create your views here.

from django.contrib.auth import get_user_model
User = get_user_model()




def playground(request):
    response = {
        'first_no':4,
        'second_no':5,
        'numbers': [1,2,3,4,5,6,7,8]
    }
    return render_to_response('playground.html', {'response': response})
 
@find_worth
def worthy(request):
    response = {}
    return render_to_response('worthy.html',{'response': response})

@find_worth
def peasant(request):
    response = {}
    return render_to_response('peasant.html',{'response': response})
def grab_item(uuid):
    return Item.objects.get(uuid=uuid).is_worthy






# Pre-defined ##############################################################

@login_required
@find_worth
def home(request):
    items = Item.objects.all()
    response={
        'all_items' : [item for item in items]
    }
    return render_to_response('home.html', {'response': response})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def grab(request, item_id):
    uuid = item_id
    request.user.is_worthy = grab_item(uuid)
    request.user.save()
    if grab_item(uuid):
        return HttpResponseRedirect('/worthy')
    else:
        return HttpResponseRedirect('/peasant')


def logout_user(request):
    logout(request)
    return redirect('home')


def login_user(request):
    response = {}
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('home'))
        else:
            messages.error(request, 'Username or password incorrect.')
    return render(request, 'login.html', {'response': response})