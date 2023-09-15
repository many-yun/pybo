import markdown
from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg


@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"] # nl2br : 줄바꿈 문자를 <br>로 바꿔줌, fenced_code : 마크다운의 소스코드 표현
    return mark_safe(markdown.markdown(value, extensions=extensions))