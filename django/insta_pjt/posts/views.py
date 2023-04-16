from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET
from .forms import PostForm, CommentForm
from .models import POST, Comment

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    post_list = POST.objects.all()
    comment_form = CommentForm()
    comments = Comment.objects.all()
    context = {
        'post_list' : post_list,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'posts/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form' : form,
    }
    return render(request, 'posts/create.html', context)

def delete(request, pk):
    post = POST.objects.get(pk=pk)
    if post.user == request.user:
        post.delete()
    return redirect('posts:index')

def update(request, pk):
    post = POST.objects.get(pk=pk)
    if post.user == request.user:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('posts:index')
        else:
            form = PostForm(instance = post)
        context = {
            'form': form,
            'post': post
        }
        return render(request, 'posts/update.html', context)
    return redirect('posts:index')

@login_required
@require_POST
def comment_create(request, pk):
    post = POST.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
    return redirect('posts:index')

@login_required
@require_GET
def comment_delete(request,post_id,comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('posts:index')

@require_POST
def like(request,post_id):
    if request.user.is_authenticated:
        post = POST.objects.get(pk=post_id)
        if post.like_users.filter(pk=request.user.pk).exists():
            post.like_users.remove(request.user)
        else:
            post.like_users.add(request.user)
        return redirect('posts:index')
    return redirect('posts:index')

@login_required
def show_likes(request):
    post_list = POST.objects.filter(like_users=request.user.pk)
    post_list = post_list.order_by('-id')
    comment_form = CommentForm()
    comments = Comment.objects.all()
    context = {
        'post_list' : post_list,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'posts/likes.html', context)

@login_required
def show_followings(request):
    post_list = POST.objects.filter(user__in=request.user.followings.all())
    post_list = post_list.order_by('-id')
    comment_form = CommentForm()
    comments = Comment.objects.all()
    context = {
        'post_list' : post_list,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'posts/followings.html', context)
