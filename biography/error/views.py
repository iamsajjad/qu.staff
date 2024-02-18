from django.views.decorators.cache import cache_page
from django.shortcuts import render

# Create your views here.

@cache_page(0)
def error404(request, exception):

    return render(request, 'error/error404.html', status=404)

@cache_page(0)
def error500(request):

    return render(request, 'error/error500.html', status=500)

