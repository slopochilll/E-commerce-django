from django.urls import URLPattern, path
from .import views

app_name= 'store'

urlpatterns=[
 path('',views.all_products, name= 'all_products')
]