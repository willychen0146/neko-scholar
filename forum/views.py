from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import Post, Comment, Account, Like, Comment_Like, Tag, Follow
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import markdown2
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
import uuid
from django.urls import reverse
from django.views.decorators.http import require_POST
from accounts.filters import CommentFilter, PostFilter
from accounts.forms import PostForm


def forum(request, category):
    posts = Post.objects.filter(category=category)
    print(posts)
    myFilter = PostFilter(request.GET, queryset=posts)
    context= {
        'posts': posts,
        'myFilter': myFilter,
        'category': category
    }
    return render(request, 'forum.html', context)

def post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comment_set.all()
    post.content = markdown2.markdown(post.content)
    user_has_liked = False
    user_has_followed = False
    if request.user.is_authenticated:
        user_has_liked = Like.objects.filter(post=post, account=request.user.account).exists()
        user_has_followed = Follow.objects.filter(following=post, follower=request.user.account).exists()

    for comment in comments:
        if request.user.is_authenticated:
            comment.user_has_liked = Comment_Like.objects.filter(comment=comment, account=request.user.account).exists()

    return render(request, 'post.html', {
        'post': post,
        'comments': comments,
        'user_has_liked_post': user_has_liked,
        'user_has_followed_post': user_has_followed,
        'no_light_css': True
    })

@login_required
def create_post_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        tags_ids = request.POST.getlist('tags')
        image = request.FILES.get('image') if 'image' in request.FILES else None

        # 保存图片
        image_path = None
        if image:
            ext = image.name.split('.')[-1]
            filename = f"{uuid.uuid4()}.{ext}"
            filepath = os.path.join(settings.MEDIA_ROOT, filename)
            with open(filepath, 'wb+') as f:
                for chunk in image.chunks():
                    f.write(chunk)
            image_path = f"{settings.MEDIA_URL}{filename}"

        post = Post.objects.create(
            title=title,
            content=content,
            category=category,
            account=request.user.account,  # 假设 Account 模型中有一个名为 account 的反向关系
            image=image_path  # 存储图片路径
        )
        post.tags.set(tags_ids)
        return redirect('post', post_id=post.id)
    tags = Tag.objects.all()
    return render(request, 'create_post.html', {'tags': tags})

def add_comment(request, post_id):
    if(request.user.is_authenticated == False):
        return redirect('login')
    post = get_object_or_404(Post, id=post_id)
    account = get_object_or_404(Account, user=request.user)
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            Comment.objects.create(
                post=post,
                account=account,
                note=comment_text,
                status='Good'  # 默认状态，可以根据需要进行调整
            )
    return redirect('post', post_id=post.id)

@login_required
def like(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        user = request.user
        like, created = Like.objects.get_or_create(post=post, account=user.account)

        if not created:
            like.delete()  # 如果已存在，删除点赞
            liked = False
        else:
            liked = True

        likes = Like.objects.filter(post=post).count()
        return JsonResponse({'liked': liked, 'likes': likes})

    return JsonResponse({'error': 'Invalid request'}, status=400)

# @csrf_exempt
# def upload_image(request):
#     if request.method == 'POST' and request.FILES.get('file'):
#         image = request.FILES['file']
#         ext = image.name.split('.')[-1]
#         filename = f"{uuid.uuid4()}.{ext}"
#         filepath = os.path.join(settings.MEDIA_ROOT, filename)

#         with open(filepath, 'wb+') as f:
#             for chunk in image.chunks():
#                 f.write(chunk)

#         image_url = f"{settings.MEDIA_URL}{filename}"
#         return JsonResponse({'success': 1, 'file': {'url': image_url}})

#     return JsonResponse({'success': 0})

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES['file']:
        image = request.FILES['file']
        post = Post(image=image)
        post.save()
        return JsonResponse({'success': 1, 'file': {'url': post.image.url}})
    return JsonResponse({'success': 0})

@require_POST
def like_comment(request, comment_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Login required'}, status=401)

    comment = get_object_or_404(Comment, id=comment_id)
    like_instance, created = Comment_Like.objects.get_or_create(comment=comment, account=request.user.account)

    if not created:
        like_instance.delete()  # 如果已存在，则删除（取消点赞）
        is_liked = False
    else:
        is_liked = True

    likes_count = Comment_Like.objects.filter(comment=comment).count()
    return JsonResponse({'liked': is_liked, 'likes_count': likes_count})

@login_required
def toggle_follow(request, post_id):
    if request.method == 'POST':
        try:
            post = Post.objects.get(id=post_id)
            obj, created = Follow.objects.get_or_create(follower=request.user.account, following=post)
            if not created:
                obj.delete()
                followed = False
            else:
                followed = True
            return JsonResponse({'followed': followed})
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)