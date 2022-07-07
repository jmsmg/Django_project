from django.urls import path, re_path, register_converter

from . import views

class YearConverter:
    regex = r'20\d{2}'

    def to_python(self, value):
        return int(value)
    
    def to_url(self, value):
        return str(value)

register_converter(YearConverter, 'year')

app_name = 'instagram' # name space 지정

urlpatterns = [
    path('', views.post_list, name='post_list'), # views.post_list 호출이 아니라 함수 그 자체를 보내야함
    path('<int:pk>/', views.post_detail),
    # path('archives/<int:year>/', views.archives_year),
    path('archives/<year:year>/', views.archives_year)
]