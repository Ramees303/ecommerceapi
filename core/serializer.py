from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class RegisterationSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=50)
    email=serializers.CharField(max_length=30,min_length=6)
    password=serializers.CharField(max_length=70,write_only=True)

    class Meta:
        model=User
        fields=['id','first_name','last_name','email','username','password']


    def validate(self, args):
        email=args.get('email',None)
        username=args.get('username',None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':('username already exists')})

        return super().validate(args)
    #super() let you acess parent class within child class


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    '** operate gathers all the named argument and makes a dictionary'
    'when calling a function ,it takes a dictionary and breaks into named arguments'
    '{x:1} fn calling x=1'


class CategorySerializer(serializers.ModelSerializer):

     class Meta:
         model=Category
         fields="__all__"

class BookSerializer(serializers.ModelSerializer):
    created_by=serializers.ReadOnlyField(source='created_by.username',read_only=False)
    'The readonlyfield is used for readonly and we cant use it in updating'
    'The source will control which arttibute needs to be populated '
    class Meta:
        model=Book
        fields=[
            'title','author','category','isbn','pages','price','stock','description','created_by',
            'status','date_created'
        ]

class ProductSerializer(serializers.ModelSerializer):
    created_by=serializers.ReadOnlyField(source='created_by.username',read_only=False)

    class Meta:
        model=Product
        fields=[
            'product_tag','name','category','price','stock','description','created_by',
            'status','date_created'
        ]


class CartUserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=('username','email')


class CartSerializer(serializers.ModelSerializer):
    cart_id=CartUserSerializer(read_only=True,many=False)
    books=BookSerializer(read_only=True,many=True)
    products=ProductSerializer(read_only=True,many=True)
    'The relationship must either set a queryset explicitly(precise and clearly expressed) '
    'or set read_only=True '

    class Meta:
        model=Cart
        fields="__all__"


class UserSerializer(serializers.ModelSerializer):
    books=serializers.PrimaryKeyRelatedField(many=True,queryset=Book.objects.all())
    products=serializers.PrimaryKeyRelatedField(many=True,queryset=Product.objects.all())
    'it is used to represent the target of relationship using its primarykey'
    class Meta:
        model=User
        fields=['id','username','books','products']