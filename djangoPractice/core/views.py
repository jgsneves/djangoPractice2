from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome):
    return HttpResponse(f'Hello {nome}!')


def soma(request, num1, num2):
    soma = num1 + num2
    mult = num1 * num2
    div = num1 / num2
    return HttpResponse(f'A soma dos números é {soma}, a multiplicação é {mult} e a divisão é {div}')


def welcome(request):
    return HttpResponse('Bem vindo!')
