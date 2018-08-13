from django.views import View
from django.shortcuts import get_object_or_404, render

def aboutView(request):
    return render(request, 'snifula/about.html')

