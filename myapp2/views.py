# myapp/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def admin_page(request):
    return render(request, 'myapp/admin_page.html')
from django.shortcuts import render

# Create your views here.
