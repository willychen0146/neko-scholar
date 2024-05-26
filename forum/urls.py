from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post/<int:post_id>/', views.post_view, name='post'),
    path('create_post/', views.create_post_view, name='create_post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('like/<int:post_id>/', views.like, name='like'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('like-comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('toggle-follow/<int:post_id>/', views.toggle_follow, name='toggle_follow'),
    path('<str:category>/', views.forum, name='to_forum'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)