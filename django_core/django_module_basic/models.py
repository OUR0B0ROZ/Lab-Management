from django.db import models
from django.utils.text import slugify
from .code_generator import generate_code
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title





# New models

class Area(models.Model):
    area_of_use = models.CharField(max_length=200)
    users = models.ManyToManyField(User, related_name='areas', blank=True)

    @property
    def user_count(self):
        return self.users.count()  # Count the number of related users

    def __str__(self):
        return self.area_of_use

class Class(models.Model):
    class_name = models.CharField(max_length=200)

    def __str__(self):
        return self.class_name

class Group(models.Model):
    group_name = models.CharField(max_length=200)

    def __str__(self):
        return self.group_name
    

class ModelTest(models.Model):
    autor = models.ForeignKey(User, 
        on_delete=models.CASCADE, 
        null=True, blank=True)
    category = models.ForeignKey(Category,
        related_name='models',
        on_delete=models.CASCADE)
    group = models.ForeignKey(Group, 
        related_name='models', 
        on_delete=models.CASCADE, 
        null=True, blank=True)
    class_model = models.ForeignKey(Class, 
        related_name='modeltests', 
        on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=10, unique=True, blank=True) # Allow it to be blank
    #Atributtes of the registred of time
    arrival_time = models.DateTimeField(blank=True, null=True)
    departure_time = models.DateTimeField(blank=True, null=True)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.code: # Generate code only if it's not already set
            self.code = generate_code()

        if not self.slug:
            self.slug = slugify(self.code)

        super(ModelTest, self).save(*args, **kwargs)
        
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    class_model = models.ForeignKey(Class, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    arrival_time = models.DateTimeField(null=True, blank=True)
    departure_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.code}"