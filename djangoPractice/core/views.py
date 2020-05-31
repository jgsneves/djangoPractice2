from django.shortcuts import render, HttpResponse
from core.models import Evento
# Create your views here.


def welcome(request):
    return HttpResponse('Bem vindo!')


def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
