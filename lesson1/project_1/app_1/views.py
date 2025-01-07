from django.shortcuts import render
from django.http import HttpResponse


def url1(request):
    return HttpResponse("ответ 1")


def url2(request):
    return HttpResponse("ответ 2")


def url3(request):
    return HttpResponse(request)
