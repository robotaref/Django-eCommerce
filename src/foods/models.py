from django.db import models
import os
import random
# Create your models here.
from .utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save
from django.urls import reverse


def get_file_name_ext(filepath):
    base_name=os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name,ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 432846232)
    name,ext = get_file_name_ext(filename)
    final_filename='{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return 'foods/{new_filename}/{final_filename}'.format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class FoodManager(models.Manager):
    def get_by_id(self, id):
        return self.get_queryset().filter(id=id)


class Food(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(default='abc',unique=True)
    price = models.BigIntegerField()
    restaurant = models.CharField(max_length=50,default='هانی')
    image = models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    city = models.CharField(max_length=50,default='تهران')

    objects = FoodManager()

    def get_absolute_url(self):
        return reverse('foods:detail',kwargs={'slug':self.slug})

    def __str__(self):
        return self.title


def food_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)


pre_save.connect(food_pre_save_receiver,sender=Food)


