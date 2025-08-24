from django.contrib import admin
from .models import Profile, Post

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')  # campos que aparecerão na listagem

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "content", "created_at")
    search_fields = ("author__username", "content")
    list_filter = ("created_at",)