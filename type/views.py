from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .randomtext import randomText

def index(request):
  return render(request,"index.html")

def randomwords(request):
  return JsonResponse(randomText())

def flag(request):
  from dotenv import load_dotenv
  import os
  load_dotenv()
  return HttpResponse(os.getenv("FLAG"))