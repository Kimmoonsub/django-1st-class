from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=128,
                                verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    # foreignkey 1대n 관계를 표현할때 쓰는 것, 글쓰는 놈 아이디 확인
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE,
                                verbose_name='작성자')
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')
    registered_dttm = models.DateField(auto_now_add=True,
                                       verbose_name='등록시간')
    
    #이거 없으면 Fcuser Object로 표시됨. 클래스를 지정된 명칭으로 반환하는 함수임
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글'