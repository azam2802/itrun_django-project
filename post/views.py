from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q

# Create your views here.
# def index(request):
#     dbPost = Posts.objects.all().order_by('?')
#     if request.method == 'POST':
#         key = request.POST.get('key')
#         dbPost = Posts.objects.filter(Q(title__icontains = key) | Q(description__icontains = key) )
#     context = {
#         "posts" : dbPost
#     }
#     return  render (request , 'index.html' , context) 

def post(request):
    dbPost = Posts.objects.all().order_by('-created')
    if request.method == 'POST':
        key = request.POST.get('key')
    context = {
        "posts" : dbPost
    }
    return  render (request , 'post/post.html' , context) 


def postId(request , id):
    dbPostId = Posts.objects.get(id = id)
    if request.method == 'POST':
    #comment
      if 'comment' in request.POST:
        text = request.POST.get('text')
        comment = PostComment.objects.create(
            users = request.user,
            post = dbPostId,
            text = text
        )
        return redirect('postId' , dbPostId.id)
    context = {
        'postId' : dbPostId
    }
    return render(request , 'post/comment.html' , context)


def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        post = Posts.objects.create(
            users = request.user,
            title = title,
            description = description,
            image = image
        )
        return redirect('index')
    return render (request , 'post/post_create.html')

def post_update(request , id):
    post = Posts.objects.get(id = id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        post = Posts.objects.get(id = id)
        post.title = title
        post.description = description
        post.image = image
        post.save()
        return redirect('postId' , post.id)
    context = {
        'post':post
    }
    return render(request, 'post/post_update.html', context)


def post_delete(request , id):
    post = Posts.objects.get(id = id)
    if request.method == 'POST':
        post = Posts.objects.get(id = id)
        post.delete()
        return redirect('index')
    context = {
        'post':post
    }
    return render (request , 'post/post_delete.html' , context)