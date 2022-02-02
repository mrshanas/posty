from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostCreateForm

# Create your views here.


@login_required
def home(request):
    """Home page of the application"""
    # display the posts of the user followed
    posts = Post.objects.filter(user=request.user)
    context = {
        'posts': posts
    }
    return render(request, 'posty/base.html', context)


@login_required
def create_post(request):
    """Post pictures"""
    if request.method != 'POST':
        form = PostCreateForm()

    else:
        form = PostCreateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('posty:home')

    return render(request, 'posty/posts/post_create.html', {'form': form})


@login_required
def display_posts(request):
    """list all user posts"""
    posts = Post.objects.filter(user=request.user)
    context = {
        'posts': posts
    }
    return render(request, 'posty/posts/posts.html', context)
