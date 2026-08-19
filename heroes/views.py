from django.shortcuts import render
from django.http import HttpResponse


def roster_view(request):
    return request, render(request, 'heroes/roster.html')

# Create your views here.
