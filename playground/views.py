from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request handler
# takes a request and return a response 

def say_hello(request):
   #returning a string that says hello world
   # return HttpResponse('Hello World')

   #returning an html template 
   #return render(request, 'hello.html')
    #dont forget to call the folder templates(plural)

    #third parameter we can pass a mapping object(dictionary)
   return render(request, 'hello.html', {'name': 'frankie'})