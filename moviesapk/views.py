from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import MovieForm
# Create your views here.
def index(request):
    obj=movies.objects.all()
    context={
        'movie_list': obj
    }
    return render(request,'index.html',context)

def details(request,movies_id):
    obj=movies.objects.get(id=movies_id)
    return render(request,'details.html',{'movie':obj })

def add(request):
    if request.method == 'POST':
        name=request.POST.get('name',)
        img=request.FILES.get('img',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        movie=movies(name=name,img=img,desc=desc,year=year)
        movie.save()
    else:
        print('error')
    return render(request,'addmovies.html')

def update(request,id):
    movie=movies.objects.get(id=id)
    form= MovieForm(request.POST ,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'movie':movie,'form':form})

def delete(request,id):
    if request.method == 'POST':
        movie=movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')