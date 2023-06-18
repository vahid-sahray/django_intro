from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('update/<int:post_id>/', views.update, name='update'),
    path('create/', views.created, name='create'),
]