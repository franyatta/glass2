from django.contrib import admin
from django.urls import path
from crystals import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.crystal_list, name='crystal_list'),
    path('add/', views.add_crystal, name='add_crystal'),
]