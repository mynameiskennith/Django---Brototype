from django.shortcuts import render
from models import MovieInfo
# Create your views here.
def create(request):
    if request.POST:
        title = request.POST.get('title')
        year = request.POST.get('year')
        desc = request.POST.get('summary')
        
    return render(request,'create.html')

def list(request):
    movie_data={'movies': [{
        'title':'Godfather',
        'year':'1990',
        'success':False,
        'img':'bat.jpg'
    },
    {
        'title':'Titanic',
        'year':'2000',
        'summary':'story of an underworld king',
        'success':False,
        'img':'cat.png'
    },
    {
        'title':'Godfather',
        'year':'1990',
        'summary':'story of an underworld king',
        'success':True,
        'img':'mind.png'

    },
    {
        'title':'GoldFish',
        'year':'1980',
        'summary':'story of an underworld king',
        'success':False,
        'img':'tvj.jpeg'
    }]
    }
    return render(request,'lists.html',movie_data)

def edit(request):
    return render(request,'edit.html')