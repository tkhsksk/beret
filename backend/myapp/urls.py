from django.urls import path
from . import views

urlpatterns = [
    # home
    path('', views.home_template, name='home'),
    # user
    path('edit/<int:pk>/', views.user_edit, name="user_edit"),
    path('search', views.search, name='search'),
]