from django.contrib import admin
from .models import Board

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    # pass
    #튜플 형태로 모델 클래스에서 필요한 필드를 표현해 줌
    list_display = ('title',)

admin.site.register(Board, BoardAdmin)