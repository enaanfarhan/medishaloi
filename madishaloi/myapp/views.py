from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Doctor, Medicine, Ambulance
from .forms import registerUser


def index(request):
    return render(request,'index.html')

#login
def getLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Username or password incorrect")
    return render(request, "user/login.html")


def getlogout(request):
    #return render(request, "login.html")
    logout(request)
    return redirect('login')

#user register

def getRegister(request):
    form = registerUser(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('login')
    return render(request, 'user/register.html', {"form": form})




##doctor
@login_required
def doctor_search_v(request):
    doctor_list = Doctor.objects.all()
    search=request.GET.get('q')
    if search:
        doctor_list=doctor_list.filter(
            Q(specialist__icontains=search)
        )
    context ={
        'doctor_list': doctor_list,
    }
    return render(request,'doctor-serach.html',context)

@login_required
def doctor_details_v(request, post_id):
    doctor_d = Doctor.objects.get(pk=post_id)
    context = {
        'doctor_d': doctor_d,
    }
    return render(request, 'doctor-profile.html', context)


##madichine
@login_required
def madichine_search_v(request):
    madichine_list = Medicine.objects.all()
    search=request.GET.get('q')
    if search:
        madichine_list=madichine_list.filter(
            Q(name__icontains=search)
        )
    context ={
        'madichine_list': madichine_list,
    }
    return render(request,'madichine/madichine-serach.html',context)

@login_required
def madichine_details_v(request, post_id):
    madichine_d = Medicine.objects.get(pk=post_id)
    context = {
        'madichine_d': madichine_d,
    }
    return render(request, 'madichine/madichine-profile.html', context)

##ambulance
@login_required(login_url='/myapp/login')
def ambulance_search_v(request):
    ambulance_list = Ambulance.objects.all()
    search=request.GET.get('q')
    if search:
        ambulance_list=ambulance_list.filter(
            Q(address__icontains=search)
        )
    context ={
        'ambulance_list': ambulance_list,
    }
    return render(request,'ambulance/ambulance-serach.html',context)

@login_required
def ambulance_details_v(request, post_id):
    ambulance_d = Ambulance.objects.get(pk=post_id)
    context = {
        'ambulance_d': ambulance_d,
    }
    return render(request, 'ambulance/ambulance-profile.html', context)