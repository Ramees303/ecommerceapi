import uuid

from django.http import HttpResponse
from rest_framework import status


from .models import *
from django.shortcuts import render
from rest_framework.response import Response
from .serializer import *
from rest_framework.decorators import api_view,permission_classes
from  rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.forms import *
# Create your views here.

class register(generics.GenericAPIView):
    serializer_class = RegisterationSerializer

    def post(self,request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "RequestId":str(uuid.uuid4()),
                "Message":"User successfully created",
                "user":serializer.data
            },status=status.HTTP_201_CREATED)
        return Response({'Errors':serializers.errors},status=status.HTTP_400_BAD_REQUEST)
'uuid are used for identifying informaton that needs to be unique within a system'
'uuid4-uses pseudo-random number generators to generate uuid'
class category(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class catdetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'



class book(generics.GenericAPIView,mixins.ListModelMixin,
           mixins.CreateModelMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class bookdetail(generics.GenericAPIView,mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    lookup_field = 'id'



    def get(self,request,id):
        return self.retrieve(id)

    def put(self,request,id):
        return self.update(request,id)

    def delete(self,request,id):
        return self.destroy(request,id)


class product(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class productdetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class cart(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class cartdetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

class ListUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes= (IsAuthenticated,)

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=(IsAuthenticated,)
    lookup_field='id'






