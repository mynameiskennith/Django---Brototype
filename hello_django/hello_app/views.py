from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def print_hello(request):
    movie_data={'movies': [{
        'title':'Godfather',
        'year':'1990',
        'success':False
    },
    {
        'title':'Titanic',
        'year':'2000',
        'summary':'story of an underworld king',
        'success':False
    },
    {
        'title':'Godfather',
        'year':'1990',
        'summary':'story of an underworld king',
        'success':True
    },
    {
        'title':'GoldFish',
        'year':'1980',
        'summary':'story of an underworld king',
        'success':False
    }]
    } 
    return render(request,'hello.html',movie_data)