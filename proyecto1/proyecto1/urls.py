from django.contrib import admin
from django.urls import path
from .views import saludo,despedida,dameFecha,calculaEdad
urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('despedida/',despedida),
    path('fecha/', dameFecha),
    path('edadfutura/<int:edad>/<int:agno>', calculaEdad),
]
