from django.urls import path
# from . import views
from .views import *

urlpatterns = [
    # login
    path('login', login.index, name='login'),
    # home
    path('', home.index, name='home'),
    # user
    path('user', user.index, name='user_index'),
    path('user/create', user.create, name='user_create'),
    path('user/edit/<int:pk>/', user.edit, name="user_edit"),
    path('user/search', user.search, name='search'),
]