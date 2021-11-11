from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
# landing page
def index(request):
    return render(request, 'pages/landingPage/index.html')

def rules(request):
     return HttpResponse("rule page")

def notablesDetail(request,notablesIndex):
     return HttpResponse("notablesDetail %s" %notablesIndex)
    
def notablesList(request):
    return HttpResponse("notablesList")

def externalLinks(request):
    return HttpResponse("externalLinks")