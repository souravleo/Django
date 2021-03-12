from django.shortcuts import render
from django.http import HttpResponse
def hi(request):
    return HttpResponse("Hello Ms Yamini!")