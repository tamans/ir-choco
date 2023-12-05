"""
URL configuration for ArtForSale project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


from chocoFinder.views import search_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("chocoFinder.urls")),
    path('search/', search_view, name='search_view'),
    path('get-chocolates/', search_view, name='get_chocolates'),
]

vue3_routes = []
if settings.DEBUG:
    vue3_routes += [
        ("vue3-root", "")
    ]


for name, route in vue3_routes:
    urlpatterns.append(path(route, TemplateView.as_view(template_name="vite-index.html"), name=name))

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)