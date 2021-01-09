from django.shortcuts import render,redirect
from datetime import datetime
from home.models import contact1
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages
from blog.models import Post1
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    
    if request.method=='POST':
        name=request.POST.get('name')
        
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('content')
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
            messages.error(request, 'Please fill the form correctly!!')
        else:
            contact=contact1(name=name,email=email,phone=phone,content=desc,timestamp=datetime.today())
            contact.save()
            messages.success(request, 'Your message is send')


        
        
    return render(request,'home/contact.html')




def search(request):
    query=request.GET['query']

    if len(query)>78:
        allposts=[]
    else:
        allposttitle=Post1.objects.filter(title__icontains=query)
        allpostcontent=Post1.objects.filter(content__icontains=query)
        allposts=allposttitle.union(allpostcontent)
       
    if len(allposts)==0:
        messages.warning(request, 'No Element is found -Please fill correctly!!')

    
    params={'allposts':allposts,"query":query}

    return render(request,'home/search.html',params)



def handlesignup(request):
    if request.method=='POST':
        username=request.POST.get('UserName')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        useremail=request.POST.get('useremail')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if len(username)>10:
            messages.error(request, 'Username must be under 10 characters')
            return redirect('home')

        if not username.isalnum():
            messages.error(request, 'Username must be Alphanumeric Only')
            return redirect('home')

        if(pass1!=pass2):
            messages.error(request, 'Password not matched')
            return redirect('home')




        myuser=User.objects.create_user(username, useremail, pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()

        messages.success(request, 'Your Account has been successfully created')
        return redirect('home')

    else:
        return HttpResponse('404 -Not Found')


def Login(request):
    if request.method=='POST':
        loginusername=request.POST.get('loginusername')
        loginpass=request.POST.get('loginpass')

        user=authenticate(username=loginusername,password=loginpass)

        if user is not None:
            login(request,user)
            messages.success(request, 'Successfully Logged In')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credential Please Try Again')
            return redirect('home')

        
    return HttpResponse('404 -Not Found')


def Logout(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('home')
        
    return HttpResponse("Logout")

