from django.contrib import admin
from django.urls import path, include
from farmacia.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('farmacia/', include('farmacia.urls')),
    path('', home, name="home"),  
]
