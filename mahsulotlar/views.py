from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_page(request):
    return render(request,'index.html')

def dasturlar_page(request):
    return HttpResponse('python js php')

def mevalar_page(request):
    return render(request, 'mevalar.html')

def kitoblar_page(request):
    return HttpResponse('badiy ilmy')