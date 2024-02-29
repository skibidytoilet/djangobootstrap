from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name="my_index"),
    path('404/', views.contact, name="my_404"),
    path('cart/', views.cart, name="my_cart"),
    path('chackout/', views.chackout, name="my_chackout"),
    path('contact/', views.contact, name="my_contact"),
    path('shop/', views.shop, name="my_shop"),
    path('shop-details/', views.shop-detail, name="my_shop-detail"),
    path('testimonial/', views.testimonial, name="my_testimonial"),

]

