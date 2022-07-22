from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 


def mostrar_base(request):
    context={}
    plantilla=loader.get_template("base.html")      
    documento= plantilla.render (context)            
    return HttpResponse(documento) 