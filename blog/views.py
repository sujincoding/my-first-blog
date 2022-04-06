from django.shortcuts import render

# Create your views here.
# 이 함수는 요청(request)을 넘겨받아 render메서드를 호출합니다. 이 함수는 render 메서드를 호출하여 받은(return) blog/post_list.html템플릿을 보여줍니다.
def post_list(request):
    return render(request, 'blog/post_list.html', {})