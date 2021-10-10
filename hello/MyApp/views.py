from django.shortcuts import redirect, render
from django.http import HttpResponse, request
# Create your views here.
context={'name':'Priyank','places':['Banglore','Jammu','Delhi','UK']}
def login(request):
    return render(request,'login.html')
def Start(request):
    login = {'name': 'priyank', 'pass': '1234'}
    name=request.GET['username']
    password=request.GET['pass']
    if(name==login['name'] and password==login['pass']):
        return render(request,'home.html',context)
    else:
        return redirect('/login/')
def Music(request):
    return render(request,'music.html')
def Places(request):
    return HttpResponse("this is Places")
def Books(request):
    return render(request,'book.html')
def Movies(request):
    return render(request,'movies.html')
def Friends(request):
    return render(request,'friends.html')
def userlogin(request):
    return render(request,'user.html',context)
def Result(request):
    res = {}
    studentResult=[{'name':'priyank','maths':99,'science':70,'eng':78,'ss':80,'total':350},
                    {'name': 'pratik', 'maths': 79, 'science': 80, 'eng': 71, 'ss': 30,'total':320},
                   {'name': 'hitesh', 'maths': 100, 'science': 81, 'eng': 51, 'ss': 60,'total':300},
                   {'name': 'manish', 'maths': 50, 'science': 51, 'eng':74, 'ss': 61, 'total': 290}]
    if request.method=='POST':
        name = request.POST['t1']
        for i in studentResult:
            if(name==i['name']):
                res=i
    return render(request, 'result.html',res)
