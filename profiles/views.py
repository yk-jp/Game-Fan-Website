from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# landing page
def index(request):
    return HttpResponse("Hello, world. You're at the profiles index.")

def rules(request):
     return HttpResponse("rule page")

def notablesDetail(request):
     return HttpResponse("notablesDetail")
    
def notablesList(request):
    return HttpResponse("notablesList")

def externalLinks(request):
    return HttpResponse("externalLinks")