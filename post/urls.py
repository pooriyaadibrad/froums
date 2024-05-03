from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='posts'),
    path('contact/', views.contact, name='post'),
    path('singlepage/<int:id>', views.singlepage, name='post'),
    path('LogIn/', views.logInView, name='post'),
]