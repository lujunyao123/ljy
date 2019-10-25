from django.shortcuts import render,HttpResponse,redirect
from app01.models import *
# Create your views here.
# from django.core.paginator import Paginator,EmptyPage

def login(request):
    username = request