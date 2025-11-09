from django.contrib import admin
from django.conf import settings
from django.urls import path, include


urlpatterns = []

if settings.ADMIN_ENABLED is True:
    urlpatterns += [path('admin_django/', admin.site.urls)]         # Web del administrador de Django

urlpatterns += [
    path('func/', include(('func.urls', 'func')), name='api_function'),         # Carga URLs de la app function
    path('class/', include(('class.urls', 'class')), name='api_class'),         # Carga la URL para la API class
]
