from distutils.command.upload import upload
from email import message
from email.policy import default
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d') # 1폴더에 파일이 몰리는 것을 방지 uload_to
    tag_set = models.ManyToManyField('Tag', blank=True) # 'Tag'로 지정하는 이유는 class Tag가 아직 읽혀지지 않았기 때문, MTM blank True로 하는 것이 좋음
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        # return f"Custom Post object ({self.id})"
        return self.message
    
    class Meta:
        ordering = ['-id']

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"


class Comment(models.Model):
    # ForeignKey(post, on_delete=models.CASCADE)도 가능
    post = models.ForeignKey('instagram.Post', on_delete=models.CASCADE) # post_id 필드 생성
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True) # 테이블에서 unique 함을 보장 받도록 함
    # post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name