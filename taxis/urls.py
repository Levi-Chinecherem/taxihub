from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.taxi_list, name='taxi_list'),
    path('add/', views.add_taxi, name='add_taxi'),
    path('<int:taxi_id>/', views.taxi_detail, name='taxi_detail'),
    path('<int:taxi_id>/edit/', views.edit_taxi, name='edit_taxi'),
    path('no_permission/', views.no_permission, name='no_permission'),
]
