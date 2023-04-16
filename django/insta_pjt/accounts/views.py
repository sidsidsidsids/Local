from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.views.decorators.http import require_GET, require_POST, require_safe
from .models import User, Profile
from .forms import CustomUserChangeForm, CustomUserCreationForm, UpdateProfileForm



# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('posts:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = { 'form':form }
    return render(request, 'accounts/signup.html', context)

def delete(request):
    if request.method == "POST":
        print("post입니다")
        request.user.delete()
        auth_logout(request)
        return redirect('posts:index')
    else:
        print("post아닙니다")
        return render(request, 'accounts/delete.html')

def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = { 'form':form }
    return render(request, 'accounts/update.html', context)

def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('posts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = { 'form':form }
    return render(request, 'accounts/password.html', context)

def profile(request, user_name):
    user = get_object_or_404(User, username = user_name)
    context = {'user': user}
    return render(request, 'accounts/profile.html', context)

def profile_update(request):
    if request.method == "POST":
        user = request.user
        profile, created = Profile.objects.get_or_create(user=user)
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', user_name = request.user.username)
    else:
        profile = request.user.profile
        form = UpdateProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'accounts/profile_update.html', context)

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_user_model().objects.get(pk=user_pk)
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
    else:
        return redirect('accounts:login')
