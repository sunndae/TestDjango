from django.urls import path
from .views import homeView, contacto, galeria

urlpatterns = [ #defino las urls acá 
                
    path('', homeView, name = 'home'),
    path('contacto/', contacto, name = 'contacto'),
    path('galeria/', galeria, name = 'galeria'),
    
]