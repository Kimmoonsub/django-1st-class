from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='태그명')

    registered_dttm = models.DateField(auto_now_add=True, verbose_name='등록시간')
    
    #이거 없으면 Fcuser Object로 표시됨. 클래스를 지정된 명칭으로 반환하는 함수임
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fastcampus_tag'
        verbose_name = '패스트캠퍼스 태그'
        verbose_name_plural = '패스트캠퍼스 태그'