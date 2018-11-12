from django.db import models
from django.contrib.auth.models import User

class CategoryGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    has_category = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    group = models.ForeignKey(CategoryGroup, on_delete=models.PROTECT)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
    def __str__(self):
        return self.name

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class PriceType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Thing(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    price_type = models.ForeignKey(PriceType, on_delete=models.PROTECT)
    price_from = models.IntegerField()
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class More(models.Model):
    id = models.AutoField(primary_key=True)
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    score = models.FloatField()
    commented_on = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.commented_by.username + ' : ' +self.description

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_on =models.DateField(auto_now_add=True)

class Stat(models.Model):
    id = models.AutoField(primary_key=True)
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Related(models.Model):
    id = models.AutoField(primary_key=True)
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    related_thing = models.ForeignKey(Thing, related_name='related_thing', on_delete=models.CASCADE)

class Recommended(models.Model):
    id = models.AutoField(primary_key=True)
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    def __str__(self):
        return self.thing.name

class File(models.Model):
    id = models.AutoField(primary_key=True)
    thing = models.ForeignKey(Thing, related_name='files', on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    file = models.FileField(upload_to='project_img')