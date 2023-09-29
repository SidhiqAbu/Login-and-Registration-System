from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import sessions 
# Create your views here.


# @login_required(login_url='login')
def HomePage(request):
    print()
    return render(request,'home.html')

# Getting login page and authentication of login credentails.....................
def LoginPage(request):
    if request.method == 'POST':
        userName = request.POST.get('userid')
        password = request.POST.get('password')
        print(userName,password)
        user = authenticate(request,username=userName,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return HomePage(request)
        else:
            return HttpResponse("Your name and password not currect..!")
            
            
    return render(request,'Login.html')



#  Getting registration page and registering user in medols function............
def SignUpPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('UserName')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        cpassword = request.POST.get('CPassword')
        print(username,email,password,cpassword)
        user = User.objects.get(username=username)
        print(user)
        if (password != cpassword):
            return HttpResponse("Password and conform password not same..!")
        else:
           try:
                return HttpResponse("username already exist!")
           except User.DoesNotExist:
                my_user = User.objects.create_user(username,email,password)
                my_user.save()
                return redirect('login/')   
    return render(request,'SignUp.html')


#  logged out function for user...........
def Logout(request):
    logout(request)
    return LoginPage(request)



