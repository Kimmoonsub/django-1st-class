from typing import Any
from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password

# forms.Form은 장고에 저장된 일반 폼이다.
class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required' : '아이디를 입력해주세요'
        },
        max_length=32, label='사용자 이름')    
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # if username and password:
        #     fcuser = Fcuser.objects.get(username=username)
        #     if not check_password(password, fcuser.password):
        #         self.add_error('password', '비번에러')
        #     else:
        #         self.user_id = fcuser.id
        # 이게 원본이며, 아래부터 예외처리 기능 들어감

        if username and password:
            try:
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist:
                self.add_error('username', '아이디가 없읍니다.')
                return
            
            if not check_password(password, fcuser.password):
                self.add_error('password', '비번에러')
            else:
                self.user_id = fcuser.id