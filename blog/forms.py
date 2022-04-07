from django import forms

from .models import Post

# 장고에 이 폼이 ModelForm이라는 것을 알려줘야해요
class PostForm(forms.ModelForm):

    # 이 폼을 만들기 위해서 어떤 model이 쓰여야 하는지 장고에 알려주는 구문입니다.
    class Meta:
        model = Post
        # 이번 폼에서는 title과 text만 보여지게 해 봅시다
        fields = ('title', 'text',)