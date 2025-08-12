from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_feed, name='home_feed'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),
]
