from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("장고 신당 훈련소에 오신걸 환영합니다.")