from django.db import models
from django.contrib.auth.models import User # 회원가입시 데이터 저장에 사용한 모델

class Question(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200) # 글자수 제한
    content = models.TextField()
    create_date = models.DateTimeField() # 작성일시
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question') # 추천인 추가

    def __str__(self):
        return self.subject

class Answer(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # ForeignKey : 다른 모델과 연결(질문 삭제될 경우 답변도 삭제)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')
