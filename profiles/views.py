from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404
from django.urls import reverse
# library
import random
# custom modules
from .assets.config import config

# Create your views here.
# landing page
def index(request):
    index = random.randint(0, len(config.get("gameType"))-1)
    gameType = config["gameType"][index]
    return render(request, 'pages/landingPage/index.html',{"index":index ,"game":config.get("games").get(gameType)})
    
def rules(request,rulesIndex):
    try:
        gameType = config["gameType"][rulesIndex]
    except Exception:
        raise Http404("Invalid request. A game rule doesn't exist.") 
    return render(request, 'pages/rulesPage/rules.html',{"index":rulesIndex ,"game":config.get("games").get(gameType)})

def notablesDetail(request,notablesIndex):
    # try:
            #  return HttpResponse("notablesDetail %s" %notablesIndex)
    return HttpResponse(reverse('notablesDetail',args={notablesIndex}))
    
def notablesList(request):
    
    return HttpResponse("notablesList")

def externalLinks(request):
    return HttpResponse("externalLinks")