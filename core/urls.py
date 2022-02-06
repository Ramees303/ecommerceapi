from django.urls import path,include
from core import views
urlpatterns = [
    path('register/',views.register.as_view(), name='register'),
    path('category',views.category.as_view(),name='category'),
    path('catdetail/<int:id>/',views.catdetail.as_view(),name='catdetail'),
    path('book',views.book.as_view(),name='book'),
    path('bookdetail/<int:id>/',views.bookdetail.as_view(),name='bookdetail'),
    path('product/',views.product.as_view(),name='product'),
    path('productdetail/<int:id>/',views.productdetail.as_view(),name='productdetail'),
    path('cart/',views.cart.as_view(),name='cart'),
    path('cartdetail/<int:pk>/',views.cartdetail.as_view(),name='cartdetail'),
    path('listuser/',views.ListUser.as_view(),name='listuser'),
    path('detailuser/<int:id>/',views.DetailUser.as_view(),name='detailuser'),
]