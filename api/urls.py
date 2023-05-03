from django.urls import path
from .views import *

urlpatterns = [
    # path('',apiOverview,name='apiOverview'),
    path('product-list',ShowAll),
    path('product-list/<int:pk>',ViewProduct),
    path('create/',CreateProduct),
    path('product-update/<int:pk>',UpdateProduct),
    path('product-delete/<int:pk>',DeleteProduct),
]