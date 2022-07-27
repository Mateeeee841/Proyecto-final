from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from .models import Publisher, pizza
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView ,DeleteView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def mostrar_base(request):
    context={}
    plantilla=loader.get_template("base.html")      
    documento= plantilla.render (context)            
    return HttpResponse(documento) 

@login_required
def ver_home(request):
    context={}
    plantilla=loader.get_template("home.html")      
    documento= plantilla.render (context)            
    return HttpResponse(documento) 
#PIZZA:
class PizzaList(LoginRequiredMixin,ListView):
    model=pizza                                  
    context_object_name="pizzas"               
    template_name="pizza/listaP.html"                     

class PizzaDetalle(LoginRequiredMixin,DetailView):
    model=pizza
    template_name="pizza/detalleP.html"

class PizzaCreacion(LoginRequiredMixin,CreateView):
    model=pizza
    success_url=reverse_lazy("Pizzas")            
    template_name="pizza/pizza_form.html"
    fields=["nombre","creador","ingredientes"]  
    
class PizzaUpdate(LoginRequiredMixin,UpdateView):
    model=pizza
    success_url=reverse_lazy("Pizzas")
    template_name="pizza/editP.html"
    fields=["nombre","ingredientes"]

class PizzaDelete(LoginRequiredMixin,DeleteView):
    model=pizza
    context_object_name="pizzas"
    template_name="pizza/deleteP.html"
    success_url=reverse_lazy("Pizzas")
class PizzaUser(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model=pizza
    context_object_name="pizzas"
    template_name="pizza/listaU.html"
#USER:
class LogIn(LoginView):
    template_name="user/panel_login.html"
    next_page=reverse_lazy("home")         

class LogOut(LogoutView):
    template_name="user/panel_logout.html"

class SignUp(SuccessMessageMixin,CreateView):
    template_name="user/singup.html"
    success_url=reverse_lazy("login")
    form_class=UserCreationForm
    success_message="Su perfil a sido creado !!"

class UserUpdate(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model=User
    template_name="user/user_form.html"
    fields=["username","email","first_name","last_name"]

    def get_success_url(self):
        return reverse_lazy("user",kwargs={"pk":self.request.user.id})

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])
    
class UserDetail(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model= Publisher
    template_name="user/user_detail.html"
    

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk']) 