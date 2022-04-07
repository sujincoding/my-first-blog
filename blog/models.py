# 모델의 필드와 정의하는 방법에 대한 장고 공식 문서
# https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types)

from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your medels here.
# 모델을 정의하는 코드
# models 은 Post가 장고 모델임을 의미하며, 이를 통해 장고는 Post가 데이터베이스에 저장되어야 한다는 것을 알게 됨
class Post(models.Model):
    # 다른 모델에 대한 링크
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 글자 수가 제한된 텍스트를 정의
    title = models.CharField(max_length=200)
    # 글자 수에 제한이 없는 긴 텍스트
    text = models.TextField()
    # 날짜와 시간을 의미
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title