from django.contrib import admin
from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateViews, ProductUpdateView, ProductDeleteView, \
    ReviewCreate

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('create/', ProductCreateViews.as_view(), name='create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
    path('<int:pk>/reviews/<int:pk>/', ReviewCreate.as_view(), name='create_review'),
]
