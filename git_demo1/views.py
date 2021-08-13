# _*_ coding:utf-8 _*_
# @Time : 2021/8/13 12:51
# @Author : xupeng
# @File : views.py
# @software : PyCharm
from django.http import HttpResponse


def index_view(request):
    return HttpResponse('hello git')
