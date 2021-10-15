from django.db import models

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=100, null=False, blank=False)
    @classmethod
    
    def search_by_title(cls,category_name):
        photo = cls.objects.filter(title__icontains=category_name)
        return photo

    def __str__(self):
        return self.name

class Photo(models.Model):
    category= models.ForeignKey(Category, on_delete=models.SET_NULL,null=True, blank=True)
    image = models.ImageField (null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description
