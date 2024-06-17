from django.db import models

# Create your models here.

class Fcuser(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name='사용자명')
    useremail = models.EmailField(max_length=128,
                                  verbose_name='사용자 이메일')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateField(auto_now_add=True,
                                       verbose_name='등록시간')
    
    #이거 없으면 Fcuser Object로 표시됨. 클래스를 지정된 명칭으로 반환하는 함수임
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자'
