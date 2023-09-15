from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin): ## 질문 검색창 생성
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
