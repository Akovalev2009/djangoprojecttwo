# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('admin-page/', views.admin_page, name='admin_page'),
]
# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('myapp.urls')),
]

