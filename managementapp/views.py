from django.shortcuts import render,redirect,HttpResponse
from .models import manage,projectlist,addusers
from django.db.models import Q
from .forms import UserForm,AdduserForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.
def tasklist(request):
         if request.user.is_authenticated:
            m=manage.objects.filter(user=request.user)
            s=len(m) > 5
            if s:
                print("limit exceed")
                
                
            q1=Q(status=1)
            q2=Q(user=request.user)
                # m=task_manage.objects.filter(user=request.user)
                # s=len(m)
                
            count_todos = m.count()
            completed_todo = manage.objects.filter(q1 & q2)
            count_completed_todo = completed_todo.count()
            uncompleted = abs(count_todos - count_completed_todo)
            content={'count_todos': count_todos,'count_completed_todo': count_completed_todo,'uncompleted':uncompleted}
            content['tasklist']=m
            
            return render(request,'index.html',content)

            # else:
            #     print("limit exceed")
            #     content={}
            #     content['error']='limit exceed'
            #     return render(request,'index.html',content)
           
         else:
            return render(request,'index.html')

def user_register(request):
    content={}
    regobj=UserForm
    print(regobj)#object bana
    content['userform']=regobj
    if request.method=='POST':
        regobj=UserForm(request.POST)
        print(regobj)#form printhora
        if regobj.is_valid():
            regobj.save()
            content['success']='User Created Successfully'
            return render(request,'user_register.html',content)

    else:
        # regobj=UserCreationForm()
        # print(regobj)
        return render(request,'user_register.html',content)

def user_login(request):
    if request.method=="POST":
        dataobj=AuthenticationForm(request=request,data=request.POST)
        print(dataobj)
        uname=dataobj.cleaned_data['username']
        upass=dataobj.cleaned_data['password']
        print('Username:',uname)
        print('Password:',upass)
        user=authenticate(username=uname,password=upass)
        print(user)
        if user:
                print('hello i am kitty')
                login(request,user)
                return redirect('/')
    else:
        lobj=AuthenticationForm
        print(lobj)
        content={}
        content['loginform']=lobj
        return render(request,'user_login.html',content)
    
def user_logout(request):

    logout(request)
    return redirect('/')

def adduser(request):
    print('innnnnnn')
    if request.method=="POST":
        ename=request.POST['uname']
        pimage=request.POST['img']
        email=request.POST['rmail']
        mob=request.POST['mob']
        quali=request.POST['quali']
        desig=request.POST['desig']
        print("Employee name:",ename)
        create=addusers.objects.create(name=ename,pimage=pimage,email=email,mobile=mob,qualification=quali,designation=desig)
        create.save()
        content={}
        content['success']='User Created Successfully'
        return render(request,'adduser.html',content)
    else:
        eobj=AdduserForm()
        # print(eobj)
        content={}
        content['form']=eobj
        return render(request,'adduser.html',content)

def displayuser(request):
    
    data=addusers.objects.all()
    content={}
    content['displayuser']=data
    return render(request,'users.html',content)


def addtask(request):
    
    if request.user.is_authenticated: 
        
        # print(u)
        if request.method=='POST':
                # print('Hello')
                t=request.POST['ttitle']
                c=request.POST['cate']
                s=request.POST['stime']
                p=request.POST['activity']
            
                if t:
                    l=task_manage.objects.create(user=request.user,task=t,type=c,Duedate=s,status=p)
                    # print(l)
                    l.save()
                         
                return redirect('/')


        else:
            # print("get block")
            l=task_manage.objects.all()
            content={}
            content['tasklist']=l
            return render(request,'addtask.html',content)
    else:
         return redirect('/login')