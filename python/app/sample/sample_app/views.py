from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #とりあえず文字列を返す。
    return HttpResponse("Indexです！")

def members(request):
	return HttpResponse("members")