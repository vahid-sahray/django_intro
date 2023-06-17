from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('detail/<int:post_id>/', views.detail),
]