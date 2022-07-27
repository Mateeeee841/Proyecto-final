from django.urls import path
from . import views 
urlpatterns =[
    path("base/",views.mostrar_base,name="base"),
    path("",views.ver_home,name="home"),
    path("pizza/",views.PizzaList.as_view(),name="Pizzas"),
    path("pizza/Crear/",views.PizzaCreacion.as_view(),name="crearP"),
    path("pizza/<pk>/",views.PizzaDetalle.as_view(),name="Pizza"),
    path("pizza/<pk>/editar/",views.PizzaUpdate.as_view(),name="editP"),
    path("pizza/<pk>/borrar/",views.PizzaDelete.as_view(),name="borrarP"),
    path("login",views.LogIn.as_view(),name="login"),
    path("logout",views.LogOut.as_view(),name="logout"),
    path("register",views.SignUp.as_view(),name="register"),
    path("user/<pk>/",views.UserDetail.as_view(),name="user"),
    path("user/<pk>/edit/",views.UserUpdate.as_view(),name="editU"),
]