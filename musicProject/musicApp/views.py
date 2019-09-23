from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a bad request. Start with the music route. ")
def music(request):
    return HttpResponse("Artists: barbra, michael, vanessa")
def barbra(request):
    return HttpResponse("Barbara Joan 'Barbra' Streisand is an American singer, actress, and filmmaker.")
def michael(request):
    return HttpResponse("Michael Bolton, known professionally as Michael Bolton, is an American singer and songwriter.")
def vanessa(request):
    return HttpResponse("Vanessa Lynn Williams is an American singer, actress, and fashion designer.")
