from django.shortcuts import render , redirect

# Create your views here.
def signup(request):
    return render(request , 'authtemp/signup.html')
def login(request):
    return render(request , 'authtemp/login.html')
def logout(request):
    return redirect('smallauth/login')
