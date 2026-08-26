from django.urls import path
from . import views

urlpatterns = [
    path('', views.roster_view, name='roster'),  # Your HTML page
    path('api/roles/<str:role_name>/',
         views.dynamic_api_view, name='dynamic_api'),
    path('roles/<str:role_name>/', views.dynamic_role_view, name='dynamic_role'),
]
