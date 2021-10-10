from io import RawIOBase
from typing import ValuesView
from django.core.checks import messages
from django.shortcuts import redirect, render
from .models import CustomerRegModel,EmployeeRegModel, Appointment, pendingAppointment
# Create your views here.
def c_signinView(request):
    return render(request,'c_signin.html')
def c_signupView(request):
    return render(request, 'c_signup.html')

def e_signupView(request):
    return render(request, 'e_signup.html')

def e_signinView(request):
    return render(request, 'e_signin.html')

def c_saveDataView(request):
    data = CustomerRegModel(name=request.GET['name'],email=request.GET['email'],password=request.GET['password'],contact=request.GET['contact'])
    data.save() 
    return redirect("/c_signin/")

def c_signInCheckView(request):
    email = request.GET['email']
    password = request.GET['password']
    data=CustomerRegModel.objects.filter(email=email,password=password)
    if data:
        name=CustomerRegModel.objects.get(email=email)
        return render(request, 'c_home.html',{'name':name.name})
    else:
        return redirect('/c_signin/')

def c_homepageView(request):
    name=request.GET['c_name']
    return render(request,'c_home.html',{'name':name})


def e_homepageView(request):
    name = request.GET['e_name']
    return render(request, 'e_home.html', {'name': name})


def e_signincheckView(request):
    email = request.GET['email']
    password = request.GET['password']
    data=EmployeeRegModel.objects.filter(email=email,password=password).count()
    if data:
        name = EmployeeRegModel.objects.get(email=email)
        return render(request,'e_home.html',{'name':name.name})
    else:
        return redirect('/e_signin/')


def e_displayAppointmentView(request):
    e_name=request.GET['e_name']
    data = Appointment.objects.filter(e_name=e_name)
    return render(request,'e_displayAppointment.html',{'data':data,'e_name':e_name})


def e_pendingAppointmentView(request):
    e_name=request.GET['e_name']
    data = pendingAppointment.objects.filter(e_name=e_name)
    return render(request, 'e_pendingAppointment.html', {'data': data,'e_name':e_name})

def e_savedataView(request):
    data = EmployeeRegModel(name=request.GET['name'], email=request.GET['email'], password=request.GET['password'],contact=request.GET['contact'], working_category=request.GET['working_category'], address=request.GET['address'])
    data.save()
    return redirect('/e_signin/')


def e_CancelRequestView(request):
    name=request.GET['name']
    id=request.GET['id']
    pendingAppointment.objects.filter(id=id).delete()
    data=pendingAppointment.objects.filter(e_name=name)
    return render(request,'e_pendingAppointment.html',{'data':data,'e_name':name})

def e_AcceptRequestView(request):
    name = request.GET['name']
    id = request.GET['id']
    delee=pendingAppointment.objects.get(id=id)
    data=Appointment(c_name=delee.c_name,e_name=delee.e_name,service=delee.service,problem=delee.problem,date=delee.date,time=delee.time)
    data.save()
    delee.delete()
    data = pendingAppointment.objects.filter(e_name=name)
    return render(request, 'e_pendingAppointment.html', {'data': data,'e_name':name})

def startpage(request):
    if(request.GET['actionname']=='signup'):
        print('signup')
    else:
        print('login')
    return render(request,'startpage.html',{'actionname':request.GET['actionname']})

def assignroleView(request):
    name=request.GET['name']
    actionname=request.GET['actionname']
    if name=='customer':
        if actionname=='login':
            return redirect('/c_signin/')
        else:
            return redirect('/c_signup/')
    else:
        if actionname=='login':
            return redirect('/e_signin/')
        else:
            return redirect('/e_signup/')


def c_selectServiceNameView(request):
    data = EmployeeRegModel.objects.filter(working_category=request.GET['service'])
    c_name=request.GET['c_name']
    print("printing.....")
    return render(request, 'c_addappoint.html', {'data': data, 'service': request.GET['service'],'c_name':c_name})

def c_addappointmentView(request):
    c_name=request.GET['c_name']
    return render(request,'c_addappoint.html',{'c_name':c_name})


def c_date_timeView(request):
    service=request.GET['service']
    name=request.GET['name']
    c_name=request.GET['c_name']
    problem=request.GET['problem']
    return render(request,'c_date_time.html',{'service':service,'c_name':c_name,'name':name,'problem':problem})

def c_selectDateView(request):
    schedule = ['10:00', '12:00', '02:00', '04:00', '06:00']
    # schedule=time_schedule
    name=request.GET['name']
    service=request.GET['service']
    date=request.GET['date']
    c_name=request.GET['c_name']
    problem=request.GET['problem']
    data=Appointment.objects.filter(e_name=name,date=date)

    for d in data:
        for i in range(len(schedule)-1):
            if d.time == schedule[i]:
                del schedule[i]
    print('schedule',schedule)
    return render(request, 'c_date_time.html', {'date':date,'schedule':schedule,'problem':problem,'name':name,'service':service,'c_name':c_name})

def c_submitAppointmentView(request):
    print(request.GET['date'], request.GET['time'],request.GET['problem'], request.GET['c_name'], request.GET['name'], request.GET['service'])
    data=pendingAppointment(c_name=request.GET['c_name'],e_name=request.GET['name'],service=request.GET['service'],problem=request.GET['problem'],date=request.GET['date'],time=request.GET['time'])
    data.save()
    return render(request,'c_home.html',{'name':request.GET['c_name']})


def c_displayappointView(request):
    c_name=request.GET['name']
    data = Appointment.objects.filter(c_name=c_name)
    data2 = pendingAppointment.objects.filter(c_name=c_name)
    return render(request,'c_display_appoint.html',{'data':data,'data2':data2,'name':request.GET['name']})


def c_deleteAppointView(request):
    delee = request.GET['id']
    c_name = request.GET['c_name']
    pendingAppointment.objects.get(id=delee).delete()
    data = Appointment.objects.filter(c_name=c_name)
    data2 = pendingAppointment.objects.filter(c_name=c_name)
    return render(request,'c_display_appoint.html',{'data':data,'data2':data2,'name':c_name})

def aboutView(request):
    return render(request,'about.html')
