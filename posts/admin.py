from django.contrib import admin

from .models import Author, Category, Post, Comment

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
# set up view count with user auth
# admin.site.register(PostView)