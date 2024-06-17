from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site

admin.site.register(FlatPage)
admin.site.register(Site)
