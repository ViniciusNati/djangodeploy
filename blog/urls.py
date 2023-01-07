from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('todos/', todos.as_view()),
    path('blog/<slug:url>/',post),
    path('category/<slug:url>/',category),
    path('',index),
    #############MTASA##############################
    path('mtaloadscreen',mtaloadscreen.as_view()),
    path('mtaacessorios',mtaacessorios.as_view()),
    path('mtaarmas',mtaarmas.as_view()),
    path('mtaavioes',mtaavioes.as_view()),
    path('mtabackups',mtabackups.as_view()),
    path('mtabases',mtabases.as_view()),
    path('mtacarros',mtacarros.as_view()),
    path('mtaconce',mtaconce.as_view()),
    path('mtacorps',mtacorps.as_view()),
    path('mtaempregos',mtaempregos.as_view()),
    path('mtafacs',mtafacs.as_view()),
    path('mtainventario',mtainventario.as_view()),
    path('mtalogin',mtalogin.as_view()),
    path('mtamapas',mtamapas.as_view()),
    path('mtamotos',mtamotos.as_view()),
    path('mtapacks',mtapacks.as_view()),
    path('mtapainel',mtapainel.as_view()),
    path('mtaroupas',mtaroupas.as_view()),
    path('mtascripts',mtascripts.as_view()),
    path('mtavelocimetros',mtavelocimetros.as_view()),
    path('search/', search),  

]  