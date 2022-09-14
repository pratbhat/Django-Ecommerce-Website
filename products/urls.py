from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products'),
    path('offers/', views.offered_products, name='offers'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('processdata/', views.process_data, name='process_data'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('myorders/', views.my_orders, name='myorders')

]
