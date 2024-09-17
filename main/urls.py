from django.urls import path
from main.views import show_main, create_product_rating

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-rating', create_product_rating, name='create_product_rating'),  
]