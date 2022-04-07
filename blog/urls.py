from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # post/<int:pk/>/는 URL 패턴을 나타냄
    # post/란 URL이 post 문자를 포함해야 함을 나타냄
    # <int:pk>는 장고는 정수 값을 기대하고 이를 pk라는 변수로 뷰로 전송하는 것을 말합니다
    # /은 다음에 / 가 한 번 더 와야 한다는 의미입니다.
    # http://127.0.0.1:8000/post/5/라고 입력하면, 장고는 post_detail 뷰를 찾아 매개변수 pk가 5인 값을 찾아 뷰로 전달합니다.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]