from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Board
from .forms import BoardForm
from fcuser.models import Fcuser
from django.http import Http404
from tag.models import Tag

# Create your views here.

# 글 고유값을 알아야 board_detail의 value에 엮어서 볼 수 있다. pk로 글 정보를 db에서 찾겠다
# 근데 pk와 db의 id는 동일하므로 아래와 같이 해도 가능
# 문법으로 강제되는 곳은 pk로 써야하지만, 실제 db에는 id로 박혀있으니(board_list에서 id 역순으로 분류함) db에서 뽑는 조건에는 id도 가능
def board_detail(request, pk):
    # 예외처리 추가, 없는 글 굳이 주소 찾아서 갈 때
    try:
        board = Board.objects.get(pk=pk)
        # board = Board.objects.get(id=pk)
    
    except Board.DoesNotExist:
        raise Http404('그런 내용 세상에 없읍니다.')

    
    # board변수에 내용을 dict 형태로 렌더링해서 html에 뿌림
    return render(request, 'board_detail.html', {'board' : board})


def board_write(request):
    # 예외처리 추가, 로그인 안하고 글쓰는 놈 있을때
    if not request.session.get('user'):
        return redirect('/fcuser/login')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            tags = form.cleaned_data['tags'].split(',')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser            
            board.save()

            for tag in tags:
                if not tag:
                    continue
                
                # ()의 조건값이 있으면 불러오고 없으면 만든다.
                # _tag 뒤에 _ 는 원래 created라는 변수인데 이번에는 안써서 _로 표시함 원래은 _tag, created였음 -> 문법확인
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list/')

    else:
        form = BoardForm()
    
    return render(request, 'board_write.html', {'form' : form})


def board_list(request):
    # '-id' -는 역순
    all_boards = Board.objects.all().order_by('-id')
    # 페이지를 긁어온다. 없으면 1로
    page = request.GET.get('p', 1)
    # 뒤에 2는 1페이지에 몇개의 글을 넣을 거냐
    paginator = Paginator(all_boards, 2)

    boards = paginator.get_page(page)
    # boards 변수는 objects로 쿼리셋 긁은 자료에다가 paginator 적용해서 페이지 정도도 가지게 됨
    return render(request, 'board_list.html', {'boards' : boards})