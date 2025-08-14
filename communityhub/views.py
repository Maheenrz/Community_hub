from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Post, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator


def home_feed(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 5)  # Show 5 posts per page

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

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

    if  request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()


    return render(request, 'communityhub/post_detail.html',{
        'post': post,
        'comments': comments,
        'form': form
    })


@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('home_feed')
    else:
        form = PostForm()
    return render(request, 'communityhub/create_post.html', {'form': form})
        


@login_required
def  edit_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post.save()    
            return redirect('post_detail', post_id=post.id)   
    else:
        post = PostForm(instance=post)

    return redirect(request, 'communityhub/edit_post.html', {'form':form})



def delete_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)

    if request.method=='POST':
        post.delete()
        return redirect('home_feed')
    return render(request, 'communityhub/delete_post.html', {'post', post})

