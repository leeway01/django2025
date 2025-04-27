from django.contrib import admin
from .models import MainContent, Comment

@admin.register(MainContent)
class MainContentAdmin(admin.ModelAdmin):
    # 'content' → 'description' 으로 교체
    list_display  = ['title', 'description', 'price', 'pub_date']
    search_fields = ['title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display  = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    # author 검색 시 username 으로 검색하도록
    search_fields = ['author__username']