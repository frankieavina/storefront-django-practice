from django.db import models
#so this model is like any other model we have in our app, but 
#this model is specifically made allowing generic relationships
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

#Generic Relationship Example 
# To define a Generic Relationship there are 3 fields we need to do:
#   1.content type
#   2.object id
#   3.content object

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TagItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # we need two attributes to identify an object outside the Tags App(find any records in any table)
    # 1. Type (product, video, article) -> we find the table
    # 2. Id of the object -> we find the record 

    #ContentType is a model that represent the type of an object in our application
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    #   LAST STEP: for generic relationships is we need to get the actual object that this tag
    #   is applied to so the actual product Product 
    content_object = GenericForeignKey()