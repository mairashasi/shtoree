from django.urls import path
from main.views import show_main, create_product_rating, show_xml, show_json, show_xml_by_id, show_json_by_id, add_product_rating_ajax
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_product_rating
from main.views import delete_product_rating

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-rating', create_product_rating, name='create_product_rating'),
    path('xml/', show_xml, name='show_xml'),  
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product-rating/<uuid:id>', edit_product_rating, name='edit_product_rating'),
    path('delete/<uuid:id>', delete_product_rating, name='delete_product_rating'),
    path('create-product-rating-ajax', add_product_rating_ajax, name='add_product_rating_ajax'),

]