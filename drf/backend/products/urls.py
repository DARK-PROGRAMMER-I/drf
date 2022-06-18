from django.urls import path
from . import views


urlpatterns = [
    #mixin urls
    # all
    path('all_products/', views.product_mixin_list_view),
    #specific mixin
    path('all_products/<int:pk>/', views.product_mixin_view),
    path('create/', views.product_create_mixin_view),
    path('update/<int:pk>/', views.product_update_mixin_view),
    path('delete/<int:pk>/', views.product_delete_mixin_view),
    #Generic class urls
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/delete/', views.product_destroy_view),
    path('<int:pk>/', views.product_detail_view),
    
    # Function base view url
    path('func/', views.product_alt_view),
    path('func/<int:pk>/', views.product_alt_view)
    
]