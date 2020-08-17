from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .randomtext import randomText

def index(request):
  return render(request,"index.html")

def randomwords(request):
  return JsonResponse(randomText())

def flag(request):
  try:
    if request.META['HTTP_REFERER'] in ["https://simpletypingtest.herokuapp.com/","http://127.0.0.1:8000/"]:
      from dotenv import load_dotenv
      import os
      load_dotenv()
      return HttpResponse(os.getenv("FLAG"))
  except:
    return HttpResponse("Dont Try to trick ME")