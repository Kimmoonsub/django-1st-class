from django.contrib import admin
from .models import Tag

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    #튜플 형태로 모델 클래스에서 필요한 필드를 표현해 줌
    list_display = ('name',)

admin.site.register(Tag, TagAdmin)
