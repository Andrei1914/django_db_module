from django.shortcuts import render
from .models import *
from .UserRegister import UserRegistrationForm
from .UserLogin import UserLoginForm
from django.core.paginator import Paginator

def all_game(request):
    game = Game.objects.all()
    return render(request, 'games.html', {'info': game})

def main_page(request):
    return render(request, 'main.html')

def basket_page(request):
    return render(request, 'basket.html')


def login_page(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = Bayer.objects.filter(name=username, password=password)
            if user:
                return render(request, 'main.html', {'info': f'{username}'})
            else:
                return render(request, 'sign_login_by_django.html', {'info': 'Неверный пароль! Или же пользователя нет в системе!'})

    form = UserLoginForm()
    return render(request, 'sign_login_by_django.html', {'form': form})
    

def registration_page(request):
        user = Bayer.objects.all()
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                repeat_password = form.cleaned_data['repeat_password']
                age = form.cleaned_data['age']
                if user.filter(name=username):
                    return render(request, 'sign_up_by_django.html', {'info': 'Пользователь уже существует'})
                elif password != repeat_password:
                    return render(request, 'sign_up_by_django.html', {'info': 'Пароли не совпадают'})
                else:
                    Bayer.objects.create(name=username, balance='10000', password=password, age=age)
                    return render(request, 'main.html', {'info': f'{username}'})
        
        form = UserRegistrationForm()
        return render(request, 'sign_up_by_django.html', {'form': form})

def viewing_news(request):
    news = News.objects.all().order_by('date')
    pg = Paginator(news, 3) 
    page_obj = pg.get_page(request.GET.get('page')) 
    return render(request, 'news.html', {'page': page_obj})