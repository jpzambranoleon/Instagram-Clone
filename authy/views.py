from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from authy.models import Profile
from django.core.paginator import Paginator
from django.urls import resolve, reverse

# Create your views here.

def UserProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    url_name = resolve(request.path).url_name

    if url_name == 'profile':
        posts = Post.object.filter(user=user).order_by('-posted')

    else:
        posts = profile.favorites.all()

    # Profile info box
    posts_count = Post.objects.filter(user=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    followers_count = Follow.objects.filter(following=user).count()

    # Follow status
    follow_status = Follow.objects.filter(following=user, follower=request).exists()

    # Pagination
    paginatior = Paginator(posts, 8)
    page_number = request.GET.get('page')
    posts_paginator = paginatior.get_page(page_number)

    template = loader.get_template('profile.html')

    context = {
        'posts': posts_paginator,
        'profile': profile,
        'following_count': following_count,
        'followers_count': followers_count,
        'posts_count': posts_count,
        'follow_status': follow_status,
        'url_name': url_name,
    }

    return HttpResponse(template.render(context, request))

