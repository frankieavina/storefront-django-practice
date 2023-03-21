from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.Models- define what the structure of our 
# db is going to look like

# many to many relationship many promotion <-> many products
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField
    #django is going to create the reverse relationship here in the promotion class
    #we will have a field set called "product_set" that return all the products for the particular promotion

class Collection(models.Model):
    title= models.CharField(max_length=255)
    # circular relationships. collection class depends on product and vice versa
    # so we solve this by circular relationships and wrap Product in quotes
    featured_product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True, related_name='+')
    # set that to plus so it wont create a collection name in the product class and have issues. So,
    # dont create the reverse relationship

    #changing the name representation of our Collection model to show in our admin site
    def __str__(self) -> str:
        return self.title
    
    #ordering our collection in admin by there title using meta class 
    class Meta:
        ordering = ['title']

#defining/shaping how our Product data is going to look.
class Product(models.Model):
    title = models.CharField(max_length=255)
    # null and blank added so when we do add its optional no necessary 
    description = models.TextField(null=True, blank=True)
    # using validators to have no negative or 0 value in unit_price when filling it out in adminSite
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, validators= [MinValueValidator(1)])
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    #one to many between one Product <-> many collection
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    #We can have multiple promotions for a Product. We are setting promotions to optional
    #  for validation when filling form in adminSite
    promotions = models.ManyToManyField(Promotion, blank= True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']

class Customer(models.Model):
    #Adding in case we ever decide to change 'G' etc 
    MEMBERSHIP_GOLD= 'G'
    MEMBERSHIP_SILVER= 'S'
    MEMBERSHIP_BRONZE= 'B'

    #Fixed list of values
    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_GOLD, 'Gold'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_BRONZE, 'Bronze')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    #in this example we have a limited list a values(G,S,B) to implement that we use choices field
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

#combining the first name with last name to display in the adminsite
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['first_name', 'last_name']

# Another example of utilizing choices field 
class Order(models.Model):
    PAYMENT_STATUS_PENDING ='P'
    PAYMENT_STATUS_COMPLETE ='C'
    PAYMENT_STATUS_FAILED ='F'

    PAYMENT_STATUS_CHOICES = [
        ( PAYMENT_STATUS_COMPLETE , 'Complete'),
        ( PAYMENT_STATUS_PENDING , 'Pending'),
        ( PAYMENT_STATUS_FAILED , 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    #protect in case we accidentally delete customer we dont delete the orders
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveBigIntegerField()
    # we have unit prices because the prices can change but we want keep the price of the item at the time of order
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


#one to one relationship between one address <-> one customer
# and a one to many relationship many addresses <-> one customer
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # if we dont have primary key we gonna end up with a one to many relationship
    # if we make this the primary key we will only have one address per customer
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    # let assume one customer can have many addresses
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)