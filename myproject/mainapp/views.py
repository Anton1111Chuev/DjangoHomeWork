from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! Первая вьюха для домашнего задания")


def about(request):
    return HttpResponse("About us - для домашнего задания")