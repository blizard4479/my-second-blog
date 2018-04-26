from django.db import models
from django.utils import timezone
# Create your models here.

''' 모든 Model 객체는 blog/model.py
파일에 선언하여 모델을 만듭니다. 이 파일에 블로그 글
모델도 정의할 거에요.
'''

class Post(models.Model): #모델을 정의하는 코드입니다. Post는 모델의 이름입니다.
# models는 Post가 장고 모델임을 의미합니다.
# 이 코드 때문에 장고는 Post가 데이터베이스에 저장되어야 한다고 알게 됩니다.

    # 다른 모델에 대한 링크를 의미합니다.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # 글자 수가 제한된 텍스트를 정의할 때 사용합니다. 글 제목같이 짧은 문자열 정보를 저장할 때 사용합니다.
    title = models.CharField(max_length=200)
    # 글자 수에 제한이 없는 긴 텍스트를 위한 속성입니다.
    # 블로그 콘텐츠를 담기 좋겠죠?
    text = models.TextField()
    # 날짜와 시간을 의미합니다.
    created_date = models.DateTimeField(
            default = timezone.now
        )
    published_date = models.DateTimeField(
            blank=True, null=True
    )


    def publish(self):
        '''
        글을 게시하는 기능입니다.
        '''
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        '''
        호출하면 Post 모델의 제목 텍스트(string)을 얻게됩니다.
        '''
        return self.title
