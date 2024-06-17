from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.board_list),
    path('write/', views.board_write),
    # 글 순서 고윳값을 확인해야 url타고 글을 읽으므로 pk값을 받음(id로 바꾸면 에러)
    path('detail/<int:pk>', views.board_detail),
]