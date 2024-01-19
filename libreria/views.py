from django.shortcuts import render,redirect
from .models import Libro
from .forms import LibroForm

# Create your views here.
# instalar conector :>pip install pymysql
# instalar conector :>pip install pillow (para las imagenes)

def inicio(request):
    return render(request,"libreria/inicio.html")

def nosotros(request):
    return render(request,"libreria/nosotros.html")

def libros(request):
    libros=Libro.objects.all()
    return render(request,"libreria/index.html",{"libros":libros})

def crear(request):
    formulario=LibroForm(request.POST or None,request.FILES or None )
    if formulario.is_valid():
        formulario.save()
        return redirect("libros")
    return render (request,"libreria/crear.html",{"formulario":formulario})

def editar(request,id):
    libro=Libro.objects.get(id=id)
    formulario=LibroForm(request.POST or None,request.FILES or None,instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect("libros")
    return render(request,"libreria/editar.html",{"formulario":formulario})

def eliminar(request,id):
    libro=Libro.objects.get(id=id)
    libro.delete()
    return redirect("libros")







