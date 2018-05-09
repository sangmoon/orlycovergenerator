from django.urls import path
from . import views


app_name = 'cover'
urlpatterns = [
    path('', views.index, name='index'),
    path('image.png/', views.image_generator, name='image_generator'),
]
