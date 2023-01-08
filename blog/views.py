from re import U
from django.http.response import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from blog.models import *
from django.core.paginator import Paginator
from random import shuffle
from django import template

def pk(request):
    return render(request,'private-key.pem')

def ct(request):
    return render(request,'certificate.pem')

def robots(request):
    return render(request, 'robots.txt')

def search(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.none()

    return render(request, 'bases/search.html', {'posts': posts})

class todos(ListView):
    #load aal the post from db(10)
    paginate_by = 19
    model = Post
    template_name = 'bases/todos.html'


def category(request,url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    data={
        'cat':cat,
        'posts':posts,

    }
    return render (request,'categorias.html',data)

def post(request,url):
    post=Post.objects.get(url=url)
    pag=Post.objects.all()
    cats=Category.objects.all()
    recente = Post.objects.order_by('-post_id')[:3]
    data={
        'post':post,
        'cats':cats,
        'pag':pag,
        'recente':recente,
    }
    
    # print(post)
    return render(request,'bases/posts.html',data)


def index(request):
    recente = Post.objects.order_by('-post_id')[:3]
    sopa={

        'recente':recente,
    }

    return render (request,'index.html',sopa)



#######################################################################################################################
############################################### MTA: SA ###############################################################
#######################################################################################################################


class mtaacessorios(ListView):
   ## posts=Post.objects.filter(title__icontains='acessorios') 
    paginate_by = 19
    model = Post
    template_name =  'mtasa/mtaacessorios.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[ACESSÓRIO]')

class mtaloadscreen(ListView):
    paginate_by = 19
    model = Post
    template_name =  'mtasa/mtaloadscreen.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[LOADSCREEN]')

class mtaarmas(ListView):
    paginate_by = 19
    model = Post
    template_name = 'mtasa/mtaarmas.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[ARMA]')

class mtaavioes(ListView):
    paginate_by = 19

    model = Post
    template_name = 'mtasa/mtaavioes.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[AVIÃO]')

class mtabackups(ListView):
    paginate_by = 19

    model = Post
    template_name = 'mtasa/mtabackups.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[BACKUP]')

class mtabases(ListView):
    paginate_by = 19

    model = Post
    template_name =  'mtasa/mtabases.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[BASE]')

class mtacarros(ListView):

    paginate_by = 19
    model = Post
    template_name =  'mtasa/mtacarros.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[CARRO]')

class mtaconce(ListView):

    paginate_by = 19
    model = Post
    template_name = 'mtasa/mtaconce.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[CONCE]')

class mtacorps(ListView):

    paginate_by = 19
    model = Post
    template_name =  'mtasa/mtacorps.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[CORP]')

class mtaempregos(ListView):


    paginate_by = 19
    model = Post
    template_name =  'mtasa/mtaempregos.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[EMPREGO]')

class mtafacs(ListView):


    paginate_by = 19
    model = Post
    template_name = 'mtasa/mtafacs.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[FAC]')
        
class mtainventario(ListView):


    paginate_by = 19
    model = Post
    template_name = 'mtasa/mtainventario.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[INVENTÁRIO]')

class mtalogin(ListView):

    paginate_by = 19
    model = Post
    template_name = 'mtasa/mtalogin.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[LOGIN]')

class mtamapas(ListView):
    paginate_by = 19

    model = Post
    template_name = 'mtasa/mtamapas.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[MAPA]')

class mtamotos(ListView):

    paginate_by = 19
    model = Post
    template_name =  'mtasa/mtamotos.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[MOTO]')

class mtapacks(ListView):

    paginate_by = 19
    model = Post
    template_name = 'mtasa/mtapacks.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[PACK]')

class mtapainel(ListView):
 
    paginate_by = 19
    model = Post
    template_name = 'mtasa/mtapainel.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[PAINEL]')

class mtaroupas(ListView):

    paginate_by = 19
    model = Post
    template_name =  'mtasa/mtaroupas.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[ROUPA]')

class mtascripts(ListView):
    paginate_by = 19

    model = Post
    template_name = 'mtasa/mtascripts.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[SCRIPT]')

class mtavelocimetros(ListView):
    paginate_by = 19

    model = Post
    template_name = 'mtasa/mtavelocimetros.html'
    def get_queryset(self):
        return Post.objects.filter(title__icontains='[VELOCIMETRO]')
#######################################################################################################################
############################################### FiveM ###############################################################
#######################################################################################################################