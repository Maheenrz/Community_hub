from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_feed, name='home_feed'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),
    path('post/new/', views.create_post_view, name='create_post'),
    path('accounts/', include('django.contrib.auth.urls')),
]
