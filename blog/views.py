from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
# 이 함수는 요청(request)을 넘겨받아 render메서드를 호출합니다. 이 함수는 render 메서드를 호출하여 받은(return) blog/post_list.html템플릿을 보여줍니다.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    # Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # form.save()로 폼을 저장하는 작업과 작성자를 추가하는 작업입니다.
            # commit=False란 넘겨진 데이터를 바로 Post 모델에 저장하지는 말라는 뜻
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            # post.save()는 변경사항(작성자 정보를 포함)을 유지할 것이고 새 블로그 글이 만들어질 거에요!
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    # 수정하고자 하는 글의 Post 모델 인스턴스(instance)로 가져옵니다.
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # 이렇게 가져온 데이터를 폼을 만들 때와(글을 수정할 때 폼에 이전에 입력했던 데이터가 있어야 하겠죠?) 폼을 저장할 때 사용하게 됩니다.
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})