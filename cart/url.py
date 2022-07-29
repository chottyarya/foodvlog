from django.urls import path
from .import views
urlpatterns=[
    path('cartdetails',views.cart_details,name='cartdetails'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('remove/<int:product_id>/',views.cart_delete,name='remove')
]