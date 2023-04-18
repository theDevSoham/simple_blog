from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('delete/<str:pk>', views.delete_post, name='delete_post'),
    path('edit/<str:pk>', views.edit_post, name='edit_post'),
    path('add', views.add_post, name='add_post'),
    path('view/<str:pk>', views.view_post, name='view_post'),
]