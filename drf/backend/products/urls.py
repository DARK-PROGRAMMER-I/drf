from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_create_view),
    
    path('all_products/', views.product_list_create_view),
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/delete/', views.product_destroy_view),
    path('<int:pk>/', views.product_detail_view)
]