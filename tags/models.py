from django.db import models
# for setting generic relationships
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tags(models.Model):
    label = models.CharField(max_length=255)

class TagItem(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey()