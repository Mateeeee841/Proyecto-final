from django import forms

#entregable
class MiHamburgesa(forms.Form):
    nombre = forms.CharField()
    contenido = forms.CharField()
    precio = forms.FloatField()
    
class MiPizza(forms.Form):
    tipo = forms.CharField()
    caracteristicas = forms.CharField()
    precio = forms.FloatField()

class MiPostre(forms.Form):
    nombre = forms.CharField()
    contenido = forms.CharField()
    precio = forms.FloatField()