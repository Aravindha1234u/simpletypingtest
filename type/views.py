from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .randomtext import randomText

def index(request):
  return render(request,"index.html")

def randomwords(request):
  return JsonResponse(randomText())

def flag(request):
  if request.META['REMOTE_ADDR'] == "127.0.0.1":
    from dotenv import load_dotenv
    import os
    load_dotenv()
    return HttpResponse(os.getenv("FLAG"))
  else:
    return HttpResponse("Dont Try to trick me")