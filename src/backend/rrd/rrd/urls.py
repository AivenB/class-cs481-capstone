"""
URL configuration for rrd project.

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
from rrd.settings import APP_ROOT   # import the APP_ROOT variable from the settings.py file

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('', include('RuralResilienceDashboard.urls')),
# ]

# Example of how to access the URLs
# http://localhost:8000/admin/
# http://localhost:8000/test/           # This accesses the test view defined in the RuralResilienceDashboard app (RuralResilienceDashboard/views.py)      

site_patterns = [
    path("admin/", admin.site.urls),
    path('', include('dashboard.urls')),  # Include the dashboard app URLs 
    # path('__reload__/', include('django_browser_reload.urls')), # (No longer needed, only for development)
]

# Update the urlpatterns to prepend the APP_ROOT to the site_patterns if APP_ROOT is not empty
if APP_ROOT:
    urlpatterns = [
        path(f'{APP_ROOT}/', include(site_patterns)),
    ]
else:
    urlpatterns = [
        path('', include(site_patterns)),
    ]