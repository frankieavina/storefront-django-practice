from django.urls import path 
#from current folder import view file
from . import views

#URLConf = url configuration
urlpatterns = [
    path('hello/', views.say_hello)
]