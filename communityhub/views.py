from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post, Profile
from django.contrib.auth.models import User


def home_feed(request):
    posts = Post.objects.all()  # Ordered by Meta ordering in model
    return render(request, 'communityhub/home_feed.html', {'posts': posts})


def profile_view(request, username):
    user_profile = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user_profile)
    posts = user_profile.posts.all()
    groups = user_profile.community_groups.all()

    return render(request, 'communityhub/profile.html',
     {'user_profile': user_profile,
     'posts': posts,
     'profile': profile,
     'groups': groups
    })

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    return render(request, 'communityhub/post_detail.html',{
        'post': post,
        'comments': comments
    })