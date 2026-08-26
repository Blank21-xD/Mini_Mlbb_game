from django.urls import path
from . import views

urlpatterns = [
    path('', views.roster_view, name='roster'),  # Your HTML page
    path('api/heroes/', views.api_roster, name='api_roster'),
    path('api/assasins/', views.api_assasins,
         name='api_assasins'),  # Your new JSON API
]
