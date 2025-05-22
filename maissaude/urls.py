"""
URL configuration for maissaude project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from paginas import views as paginas_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('login/', paginas_views.login_view, name='login'),
path('admin/', admin.site.urls),
path('', paginas_views.index, name='index'),
path('', include("paginas.urls")),
path('cadastro/', paginas_views.cadastro_view, name='cadastro'),
path('accounts/', include("django.contrib.auth.urls")),
path('accounts/register/', paginas_views.register, name='cadastro'),
path('dashboard/', paginas_views.dashboard_main, name='dashboard_main'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)