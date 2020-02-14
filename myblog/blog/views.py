from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def index(request):
     # return HttpResponse('helloworld')
    articles=models.Artical.objects.all();
    return render(request, 'blog/index.html',{'articles':articles})


def article_page(request,article_id):
    article=models.Artical.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

def article_edit(request):
    return render(request,'blog/Edit_page.html')

def edit_action(request):
    title=request.POST.get('title','TITLE')
    content=request.POST.get('content','CONTENT')
    models.Artical.objects.create(title=title,content=content)
    articles = models.Artical.objects.all();
    return render(request, 'blog/index.html', {'articles': articles})