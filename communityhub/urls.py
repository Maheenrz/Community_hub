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
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('group/', views.groups, name='groups'),
    path('group/<int:group_id>/', views.group_detail, name = 'group_detail'),
    path('group/<int:group_id>/join/', views.join_group, name='join_group'),
    path("inbox/", views.inbox, name="inbox"),
    path("send/<str:username>/", views.send_message, name="send_message"),

]
