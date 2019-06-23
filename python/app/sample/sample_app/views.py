from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #とりあえず文字列を返す。
#    return HttpResponse("Indexです！")
  variable1 = 100
  return render(request, 'sample_app/index.html',{'a':variable1})

def members(request):
  return HttpResponse("members")