from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='posts'),
    path('contact/', views.contact, name='post'),
    path('singlepage/<int:id>', views.singlepage, name='singlepage'),
    path('LogIn/', views.logInView, name='LogIn'),
    path('LogIn1/<int:id>', views.logInView1, name='LogIn'),
    path('LogInReq/', views.Login, name='LogInReq'),
    path('LogOut/', views.LogOut, name='LogOut'),
    path('signIN/', views.signIN, name='signIN'),
    path('comment/<int:id>', views.commentRegister, name='comment'),
    path('signInReq/', views.signInReq, name='signInReq'),
]