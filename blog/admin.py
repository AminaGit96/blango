from django.contrib import admin
from blog.models import Tag, Post
from django.contrib import admin
from blog.models import Tag, Post, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)