from turtle import update
from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    message = models.TextField()
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        #return f'Custom Post object ({self.id})'
        return self.message
    
    # 인자 없는 속성 지정 가능 (admin단 에서도 구현 가능하나 자주 사용할 경우 model단에서 활용)
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"