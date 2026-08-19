from django.urls import path
from . import views

urlpatterns = [
    path('', views.roster_view, name='roster'),
]
