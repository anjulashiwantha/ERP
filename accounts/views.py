from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .form import *
from .filters import *


# Create your views here.

def Register(requst):
    form = CreateUserForm()
    if requst.method == 'POST':
        form = CreateUserForm(requst.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            role = form.cleaned_data.get('permission')
            group = Group.objects.get(name=role)
            user.groups.add(group)

            messages.success(requst, 'Account was created for ' + username)
            return redirect("home")

    context = {'form': form}
    return render(requst, 'accounts/registor.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.groups.filter(name='Admin').exists():
                return redirect("Admin_Dashboard")
                print(user.groups.all())
            else:
                return redirect("home")


        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect("login_page")


def admindashboard(requst):
    user = UserCreated.objects.all()
    owners = create.objects.all()
    context = {'user': user, 'owners': owners}
    return render(requst, 'accounts/ad_dashboard.html', context)


def CreatedUser(requst):
    if requst.method == "GET":
        form = createdUser()
        context = {'form': form}
        return render(requst, 'accounts/User_form.html', context)
    else:
        form = createdUser(requst.POST)
        if form.is_valid():
            form.save()
        return redirect('Admin_Dashboard')


def searchUser(requst):
    user = UserCreated.objects.all()

    myFilter = userFilter(requst.GET, queryset=user)
    users = myFilter.qs

    context = {'users': users, 'myFilter': myFilter}
    return render(requst, 'accounts/search_user.html', context)

def userdelete(requst, user_id):
    users = UserCreated.objects.get(id=user_id)
    if requst.method == 'POST':
        users.delete()
        return redirect('Search_User')
    context = {'users': users}
    return render(requst, 'accounts/ad_delete.html', context)



def home(requst):
    owners = create.objects.all()
    context = {'owners': owners}
    return render(requst, 'accounts/dashboard.html', context)


def Order_Form(requst):
    if requst.method == "GET":
        form = creat()
        context = {'form': form}
        return render(requst, 'accounts/order.html', context)
    else:
        form = creat(requst.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


def OrderDelete(requst, pk):
    owner = create.objects.get(id=pk)
    if requst.method == 'POST':
        owner.delete()
        return redirect('Search_x')
    context = {'owner': owner}
    return render(requst, 'accounts/delete.html', context)


def Search(requst):
    owners = create.objects.all()

    myFilter = OrderFilters(requst.GET, queryset=owners)
    owners = myFilter.qs

    context = {'owners': owners, 'myFilter': myFilter}
    return render(requst, 'accounts/Search.html', context)

def Update(requst, pk):
    owners = create.objects.get(id=pk)
    form = creat(instance=owners)
    if requst.method == 'POST':
        form = creat(requst.POST, instance=owners)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(requst, 'accounts/order.html', context)
