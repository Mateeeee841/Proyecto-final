from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from app0.models import  Hambuergesa,Pizza,Postre
from app0.forms import  MiHamburgesa,MiPizza,MiPostre


def mostrar_index(request):
    return render(request,"mi_app/index.html",{"mi_titulo":"Hola mi primer website!"})

def hamburgesa_formulario(request):
    if request.method == "POST":
        miformulario = MiHamburgesa(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            hamburgesa = Hambuergesa(nombre=informacion["nombre"],contenido=informacion["contenido"],precio=informacion["precio"])
            hamburgesa.save()
            return render(request,"mi_app/index.html")

    else:
        miformulario = MiHamburgesa()

    return render(request,"mi_app/hamburgesa.html",{"miformulario":miformulario})

def pizza_formulario(request):
    if request.method == "POST":
        miformulario_pizza = MiPizza(request.POST)
        print(miformulario_pizza)
        if miformulario_pizza.is_valid:
            informacion_pizza = miformulario_pizza.cleaned_data
            pizza = Pizza(tipo=informacion_pizza["tipo"],caracteristicas=informacion_pizza["caracteristicas"],precio=informacion_pizza["precio"])
            pizza.save()
            return render(request,"mi_app/index.html")

    else:
        miformulario_pizza = MiPizza()

    return render(request,"mi_app/pizza.html",{"miformulario_pizza":miformulario_pizza})


def postre_formulario(request):
    if request.method == "POST":
        miformulario_postre = MiPostre(request.POST)
        print(miformulario_postre)
        if miformulario_postre.is_valid:
            informacion_postre = miformulario_postre.cleaned_data
            postre = Postre(nombre=informacion_postre["nombre"],contenido=informacion_postre["contenido"],precio=informacion_postre["precio"])
            postre.save()
            return render(request,"mi_app/index.html")

    else:
        miformulario_postre = MiPostre()

    return render(request,"mi_app/postre.html",{"miformulario_postre":miformulario_postre})

def leer_piza(request):
    pizza = Pizza.objects.all()
    contexto = {"pizza":pizza}
    return render(request,"mi_app/leer_pizza.html",contexto)

def eliminar_postre(request,nombre_postre):
    postre = Postre.objects.get(nombre=nombre_postre)
    postre.delete()

    postre = Postre.objects.all()
    contexto = {"postre":postre}
    return render(request,"mi_app/postre.html",contexto)


def editar_hamburgesa(request,hamburgesa_nombre):
    hamburgesa = Hambuergesa.objects.get(nombre=hamburgesa_nombre)
    if request.method == "POST":
        miformulario = MiHamburgesa(request.POST)

        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            hamburgesa.nombre = informacion["nombre"]
            hamburgesa.contenido = informacion["contenido"]
            hamburgesa.precio = informacion["precio"]

            hamburgesa.save()

            return render(request,"mi_app/index.html")
    else:
        miformulario = MiHamburgesa(initial={"nombre":hamburgesa.nombre,"contenido":hamburgesa.contenido,"precio":hamburgesa.precio})

    return render(request,"mi_app/editar-hamburgesa.html",{"miformulario":miformulario,"hamburesa_nombre":hamburgesa_nombre})

