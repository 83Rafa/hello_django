from django.shortcuts import render, HttpResponse

# Create your views here.

def soma(request, numeroa, numerob):
    soma = numeroa + numerob
    return  HttpResponse('<h1>A Soma de {} com {} dá: {}</h1>'.format(numeroa, numerob, soma))

def subtracao(request, numeroa, numerob):
    subtracao = numeroa - numerob
    return  HttpResponse('<h1>A Subtração de {} com {} dá: {}</h1>'.format(numeroa, numerob, subtracao))

def multiplicacao(request, numeroa, numerob):
    multiplicacao = numeroa * numerob
    return HttpResponse('<h1>A Multiplicação de {} com {} dá: {}</h1>'.format(numeroa, numerob, multiplicacao))

def divisao(request, numeroa, numerob):
    divisao = numeroa / numerob
    return HttpResponse('<h1>A Divisão {} por {} dá: {}</h1>'.format(numeroa, numerob, divisao))





