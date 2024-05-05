from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='posts'),
    path('contact/', views.contact, name='post'),
    path('singlepage/<int:id>', views.singlepage, name='singlepage'),
 #   path('LogIn/<string:message>', views.logInView, name='LogIn'),
    path('LogInReq/', views.Login, name='LogInReq'),
    path('LogOut/', views.LogOut, name='LogOut'),
]