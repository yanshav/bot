from django.shortcuts import render
from .models import Users
from selenium import webdriver
import time, random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .seleniumbot import Bot


# Create your views here.

def home_page(request):
    return render(request, 'home.html')


def work(request):
    name = request.POST['name']
    password = request.POST['password']
    # check_object = Bot(name, password)
    # if check_object.check(name, password):
    #     user = Users(name=name, password=password)
    #     user.save()
    #     return render(request, 'work.html', {'name': name})
    # else:
    #     return render(request, 'error.html')

    user = Users(name=name, password=password)
    user.save()
    return render(request, 'work.html', {'name': name})


def error(request):
    return render(request, 'error.html')


def rec(request):
    return render(request, 'rec.html')


def end_follow(request):
    print('tut------------------------')
    hashtag = request.POST['hash']
    numb = request.POST['numb']
    name = Users.objects.order_by('-id')[0].name
    password = Users.objects.order_by('-id')[0].password
    bot = Bot(name, password)
    bot.follow(hashtag, numb)
    if bot.status == 'error':
        bot.close_browser()
        return render(request, 'error.html')
    time.sleep(2)
    bot.close_browser()
    login_users = bot.list_name
    return render(request, 'end.html', {'name': name,
                                        'login_users': login_users,
                                        'work': 'Вы подписались на следующих пользователей'})


def end_like(request):
    hashtag2 = request.POST['hash']
    numb = request.POST['numb']
    print('request', hashtag2)
    print('reqq', numb)
    name = Users.objects.order_by('-id')[0].name
    password = Users.objects.order_by('-id')[0].password
    bot = Bot(name, password)
    bot.like(hashtag2, numb)
    if bot.status == 'error':
        bot.close_browser()
        return render(request, 'error.html')
    time.sleep(2)
    bot.close_browser()
    login_users = bot.list_name
    return render(request, 'end2.html', {'name': name,
                                         'login_users': login_users,
                                         'work': 'Вы поставили лайки следующим пользователям'})


def end_comment(request):
    print('++++++++++++++++++++++++++++++++')
    hashtag = request.POST['hash']
    numb = request.POST['numb']
    name = Users.objects.order_by('-id')[0].name
    password = Users.objects.order_by('-id')[0].password
    comments = request.POST['text']
    bot_comment = Bot(name, password)
    bot_comment.comments(hashtag, numb, comments)
    if bot_comment.status == 'error':
        bot_comment.close_browser()
        return render(request, 'error.html')
    time.sleep(2)
    bot_comment.close_browser()
    login_users = bot_comment.list_name
    return render(request, 'end.html', {'name': name,
                                        'login_users': login_users,
                                        'work': 'Вы оставили коментарии следующим пользователям'})
