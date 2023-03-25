from django.shortcuts import render, redirect
from .forms import PostForm
from .models import POST

# Create your views here.
def index(request):
    post_list = POST.objects.all()
    context = {
        'post_list' : post_list
    }
    return render(request, 'posts/index.html', context)

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form' : form
    }
    return render(request, 'posts/create.html', context)

def delete(request, pk):
    post = POST.objects.get(pk=pk)
    post.delete()
    return redirect('posts:index')

def update(request, pk):
    post = POST.objects.get(pk=pk)
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