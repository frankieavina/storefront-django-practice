from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
# request handler
# takes a request and return a response 

def say_hello(request):

   ################### part 1 Views Intro##################################
   #returning an html template 
   #return render(request, 'hello.html')
   #dont forget to call the folder templates(plural)

   #returning a string that says hello world
   # return HttpResponse('Hello World')

   #third parameter we can pass a mapping object(dictionary)
   #return render(request, 'hello.html', {'name': 'frankie'})

   ####################### part 2 ORM #######################################
   # Our manager object is Product.objects 
   # in this case .all method returns a queryset
   # query_set = Product.objects.all()

   #Three scenerios where querysets are evaluated
   #1. when we iterate over a queryset 
   # for product in query_set:
   #    print(product)

   #2. when we convert it to a list 
   # list(query_set)

   #3. when we access and individual element or slice it
   # query_set[0], query.set[0:n]

   # retrieving an object not a queryset 
   # try: 
   #    product = Product.objects.get(pk=1)
   # except ObjectDoesNotExist:
   #    pass

   #filtering objects using look up types (lt, gte, lte, gt)
   # this example we want to find all the products that contain coffee in the title
   query_set = Product.objects.filter(title__contains = 'coffee')


   return render(request, 'hello.html', {'name': 'frankie', 'products': list(query_set)})



