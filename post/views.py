from django.shortcuts import render,redirect
from . import models
from django.contrib.auth import authenticate, login, logout
from . import loginForm
from django.contrib import messages
# Create your views here.
def index(request):
    posts = models.post.objects.all().order_by('-id')

    users = models.user.objects.all()
    videos = models.videoclass.objects.all()
    for user in users:
        user.password=0
    return render(request, 'index.html',context={'posts':posts,'users':users,'videos':videos})
def blog(request):
    posts = models.post.objects.all().order_by('-id')
    return render(request, 'blog.html',context={'posts':posts})
def contact(request):
    return render(request=request,template_name='Contact_us.html')
def singlepage(request,id):
    post=models.post.objects.get(id=id)
    return render(request=request,template_name='single.html',context={'post':post})
def logInView(request,message):
    form = loginForm.LoginForm()
    if message== 'sendMessage':
        messages.success(request,'لظفا برای نوشتن نظر اول وارد شوید !')
        return render(request=request, template_name='loginForm.html', context={'form': form})

    return render(request=request,template_name='loginForm.html',context={'form':form})
def Login(request):
    posts = models.post.objects.all().order_by('-id')

    users = models.user.objects.all()
    videos = models.videoclass.objects.all()
    for user in users:
        user.password = 0
    if request.method=='POST':
        form=loginForm.LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(username=email,password=password)
            login(request,user)
            messages.success(request,'با موفقیت وارد شدید!')
            return render(request=request,template_name='index.html',context={'posts':posts,'users':users,'videos':videos})
        else:
            messages.error(request,'در ورود شما مشکلی پیش آمد!')
            return redirect('login')
def LogOut(request):
    logout(request)
    messages.success(request,'خروج شما موفق بود!')
    return redirect ('index')
