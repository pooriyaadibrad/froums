from django.shortcuts import render
from . import models
from django.contrib.auth import authenticate, login, logout
from . import loginForm
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
def logInView(request):
    form=loginForm.LoginForm()
    return render(request=request,template_name='loginForm.html',context={'form':form})