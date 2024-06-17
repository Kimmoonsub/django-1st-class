from django.contrib import admin
from.models import Fcuser
# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    # pass
    #튜플 형태로 모델 클래스에서 필요한 필드를 표현해 줌
    list_display = ('username','useremail' ,'password', 'registered_dttm')

admin.site.register(Fcuser, FcuserAdmin)