from . import views
from django.urls import path
app_name='ecomapp'


urlpatterns = [
    path('',views.AllProdCat,name='AllProdCat'),
    path('ecomapp/<slug:c_slug>/', views.AllProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:prod_slug>/', views.prodCatDeet, name='prodCatDeet'),

]