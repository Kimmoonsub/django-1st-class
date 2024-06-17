from typing import Any
from django import forms

# forms.Form은 장고에 저장된 일반 폼이다.
class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required' : '제목을 입력해주세요'
        },
        max_length=128, label='제목')    
    contents = forms.CharField(
        error_messages={
            'required' : '내용을 입력해주세요.'
        },
        widget=forms.Textarea, label='내용')
    tags = forms.CharField(
        required=False, label='태그')