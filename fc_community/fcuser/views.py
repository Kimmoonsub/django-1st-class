from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm

# Create your views here.

def home(request):
    # 이하 내용은 home.html으로 이동
    ### pk ### login함수에서 세션값을 db로부터 확인한 사용자 id로 저장하였기 때문에 정보를 다시 불러옴
    # user_id = request.session.get('user')

    # 세션으로부터 사용자id가 get이 되면(즉 로그인 했다면)
    # if user_id:
    #     # fcuser라는 변수는 db에서 주요 키로 user_id(db에서 확인한 사용자 id로 저장한 세션 id)로 검색한 사용자 정보
    #     fcuser = Fcuser.objects.get(pk=user_id)
        
    return render(request, 'home.html')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])    
    return redirect('/')

def login(request):
    if request.method == 'POST':
        # .session처럼 request뒤에 .POST 붙여서 포스트 받은 데이터를 loginform클래스에 넣음
        form = LoginForm(request.POST)
        # 빌트인 된 기본적인 유효성 검사
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})
    # if request.method == 'GET':
    #     return render(request, 'login.html')
    # elif request.method == 'POST':
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)

    #     res_data = {}
    #     if not (username and password):
    #         res_data['error'] = '값을 다 입력하시오.'
    #     else:
    #         # 앞에가 model의 Fcuser로부터 뒤에가 html로부터 
    #         fcuser = Fcuser.objects.get(username=username)
    #         if check_password(password, fcuser.password):
    #             #### pk ###세션값을 설정 = 위의 objects.get으로 db에서 찾은 사용자 id로 저장함
    #             request.session['user'] = fcuser.id
    #             # 이라믄 홈으로 이동
    #             return redirect('/')
    #         else:
    #             res_data['error'] = '비밀번호가 틀렸습니다.'

    #     return render(request, 'login.html', res_data)

# register라는 함수에 request라는 변수 -> url에 연결하면 요청 정보가 request를 통해서 함수로 작업됨
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        # register.html에서 정리한 name 값으로 움직임
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        # 딕셔너리로 두고 이하의 조건식에서 error : 메세지로 만든 다음, 마지막 render 함수에서 html에 전달, html의 {{ error }}에 표시
        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '값을 다 입력하시오.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        
        # 앞에 username, password : model.py의 Fcuser클래스의 변수
        # 뒤에 username, password : html에서 name 값으로 전달 받은 register 함수에 정의 된 변수
        else:
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )
            fcuser.save()

        return render(request, 'register.html', res_data)