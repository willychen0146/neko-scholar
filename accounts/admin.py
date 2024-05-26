from django.contrib import admin
from .models import *

admin.site.register(Account)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follow)
admin.site.register(Setting)
admin.site.register(Message)
admin.site.register(Comment_Like)