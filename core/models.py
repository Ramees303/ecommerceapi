from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=200)

    class Meta:
        verbose_name_plural='categories'

    def __str__(self):
        return self.title


class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200,default='Charles')
    category=models.ForeignKey(Category,related_name='books',on_delete=models.CASCADE)
    'The related_name :-specifies the name for the reverse relation '
    'from the category model back to book model'
    isbn=models.CharField(max_length=13) #it is 13 digitcombination in book
    pages=models.IntegerField()
    price=models.IntegerField()
    stock=models.IntegerField()
    description=models.TextField()
    created_by=models.ForeignKey('auth.User',related_name='books',on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
    date_created=models.DateField(auto_now_add=True)


    class Meta:
        ordering=['-date_created'] #To define the ordering of objects of a model
        #THE last created will come first


    def __str__(self):
        return self.title

class Product(models.Model):
    product_tag=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    created_by=models.ForeignKey('auth.User',related_name='products',on_delete=models.CASCADE)
    'NULL=True means there is no constrait(limitation) of database for the field to be filled'
    'so you can have an object with null value for the filled that has this option'
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{}{}'.format(self.product_tag,self.name)
    # string formating:-it is a process of inserting a custom string in
    #predefined text

class Cart(models.Model):
    cart_id=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    on_created=models.DateTimeField(auto_now_add=True)
    books=models.ManyToManyField(Book)
    products=models.ManyToManyField(Product)

    class meta:
        ordering=['cart_id','-on_created']


    def __str__(self):
        return f'{self.cart_id}'


