from django.views.generic import ListView
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Post
# Create your views here.

post_list = ListView.as_view(model=Post) # 아래 포스트 리스트 전체 읽어오기 가능하되 검색은 안됨

# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)

#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,        
#     })

def post_detail(request:HttpRequest, pk:int) -> HttpResponse:
    response = HttpResponse()
    response.write("Hello World")
    return render(request, 'instagram/post_list.html', {})

def archives_year(request, year):
    return HttpResponse(f'{year}년 arhcive')