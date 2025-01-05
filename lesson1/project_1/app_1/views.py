from django.shortcuts import render
from django.http import HttpResponse


def url1(reqest):
    return HttpResponse("ответ 1")

def url2(reqest):
    return HttpResponse("ответ 2")

def url3(reqest):
    return HttpResponse("ответ 3")
