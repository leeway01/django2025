from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:content_id>/', views.detail, name='detail'),
    path('comment/create/<int:content_id>/', views.comment_create, name='comment_create'),
    path('comment/update/<int:comment_id>/', views.comment_update, name='comment_update'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('product/', views.product_list, name='list'),
    path('category/<str:category>/', views.product_list, name='list_by_category'),
    path('order/<int:product_id>/', views.product_order, name='order'),
]
