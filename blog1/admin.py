from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at']
    search_fiedls = ['message']
    
    # admin, model에서 어느 곳에서나 구현 가능
    def message_length(self):
        return len(self.message)
    message_length.short_description = "메세지 글자수"