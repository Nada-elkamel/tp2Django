
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
  template = loader.get_template('accueil.html')
  context = {
    'nom': 'El Kamel', 
    'prenom': 'Nada' ,
    'age' : 20,
    'sexe' : 'F',
    'adresse': 'Nabeul',
    'classe' : 'DSI23',
    'notes' : [12,15,5,17.5,0,10.75],
}           
  return HttpResponse(template.render(context, request))

def consulter(request):
  template = loader.get_template('notes.html')
  context = {
    'nom': 'El Kamel', 
    'prenom': 'Nada' ,
    'sexe' : 'F',
    'notes' : [],
    
  }
  return HttpResponse(template.render(context,request))


def retourner(request):
    return HttpResponseRedirect(reverse('index'))