#encoding:utf-8

from principal.models import Receta, Comentario
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User 

def sobre(request):
    html="<html><body>Aplicació Exemple de Maestros  </body></html>"
    return HttpResponse(html)

def inicio(request):
    recetas = Receta.objects.all()
    return render_to_response("inicio.html",{"recetas":recetas})

def usuarios(request):
    usuarios = User.objects.all()
    recetas = Receta.objects.all()
    return render_to_response("usuarios.html",{"recetas":recetas,"usuarios":usuarios})

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render_to_response("lista_recetas.html",{"recetas":recetas}, context_instance= RequestContext(request))

def detalle_receta(request,id_receta):
    dato = get_object_or_404(Receta, pk = id_receta)
    comentarios = Comentario.objects.filter(receta = dato)
    return render_to_response("receta.html",{"receta":dato,"comentarios":comentarios},context_instance = RequestContext(request))

