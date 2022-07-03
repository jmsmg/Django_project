from django.contrib import admin
from .models import Post, Comment, Tag
from django.utils.safestring import mark_safe

# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'is_public', 'message_length', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message'] # 검색기능

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px" />') # mark_safe로 감싸주지 않으면 사진을 노출시키지 않음
        return None

    # 모델에서 구현
    def message_length(self, post):
        return f'{len(post.message)} 글자'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass