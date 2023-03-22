from django.contrib import admin, messages
from django.http import HttpRequest
from . import models
from django.db.models import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from django.contrib.contenttypes.admin import GenericTabularInline
from tags.models import TagItem

########------------------------------------------------------------------##################
# adding a section in product admin to manage the tags for the product object
class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TagItem 

#customizing List Page from modeladmin
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    #customize the fields we want to show in the forms by using 
    # fields, exclude, and readonly_fields attribute (also autocomplete_fields, prepopulated_fields)
    # fields = ['']
    # exclude = ['']
    # readonly = []
    actions = ['clear_inventory']
    inlines = [TagInline]
    list_display = ['title', 'unit_price', 'collection_title', 'inventory_status']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    #adding filtering. these will filter by collection and last update
    list_filter = ['collection', 'last']

    def collection_title(self,product):
        return product.collection.title
    
    #adding a computed column that will show low or ok depending on inventory
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'Ok'
    
    # we are creating a new dropdown actions that will clear the inventory 
    # or set the inventory=0 of the selected products and get a message
    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated',
            messages.ERROR
        )


########------------------------------------------------------------------##################
# Register your models here.
#admin.site.register(models.Collection)

#Register Product 
# dont need since the decorator takes care of it
# admin.site.register(models.Product)

########------------------------------------------------------------------##################
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10
    # adding search to the list page and using 'look up type' to search a specific area/word etc.
    search_fields = ['first_name_startswith', 'last_name__startswith']

########------------------------------------------------------------------##################
# creating this class to include in orderAdmin to manage the orders 
# we can also have StackedInline and now each item will have its own form
# so, Product: _____ , newline: Quantity: ______, newline Unit price: ______ 
class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    autocomplete_fields = ['products']
    # so by default we sill have 0 order items to start with
    extra = 0
# this will have a new order list in the admin page with the order ids
# and placed date and the related object(Customer object) customer name which we defined 
# the custom order and string in the models.py under the customer class
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
    #creates an autocomplete field so we can search(add something to models to allow search)
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]

########------------------------------------------------------------------##################
# in this example we dont have an field(s) called products_count stored in 
# collection object
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields = ['title']
 
    def products_count(self, collection):
        #return collection.products_count
        # part 2 consist of instead of returning a number we will return a string 
        # with an html string(the number(s) of the products_count)
        # to direct it to the right page use reverse:nameofapp_nameofmodel_nameofpage
        # now we need to apply a filter '?collection_id:1' so now the link will only take us 
        # to the selected collection
        url = (
            reverse('admin:store_product_changelist') 
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            })
        )
        return format_html('<a href="{}">{}</a>',url, collection.products_count)
        
    
    # we need to overide the query set and annotate/add on our collections with the number
    # of there products.(so add products_count=Count('product') to the Collection object) 
    # So every ModelAdmin has a method get_queryset 
    @admin.display(ordering='products_count')
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )