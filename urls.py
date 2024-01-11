from django.urls import path
from .views import create_item, read_item, update_item, delete_item

urlpatterns = [
    path('api/create/', create_item, name='create_item'),
    path('api/read/<int:item_id>/', read_item, name='read_item'),
    path('api/update/<int:item_id>/', update_item, name='update_item'),
    path('api/delete/<int:item_id>/', delete_item, name='delete_item'),
]
