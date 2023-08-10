from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('upload/', views.upload_image, name='upload'),
    path('delete/<int:pk>/', views.delete_image, name='delete_image'),
]
