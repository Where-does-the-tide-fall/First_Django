from django.shortcuts import render
from django.http import HttpResponse
from users.models import User


# Create your views here.
from django.http import HttpResponse


# /register/
def register(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'username:{username}, password:{password}')
        user = User.objects.create(username=username,password=password)
        return HttpResponse('注册成功')