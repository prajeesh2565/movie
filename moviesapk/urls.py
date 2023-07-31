from django.contrib import admin
from django.urls import path,include
from . import views

# namespace
app_name = 'moviesapk'

urlpatterns = [
    path('',views.index,name='index'),
    path('movies/<int:movies_id>',views.details,name='details'),
    path('add/',views.add,name='add_movies'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]