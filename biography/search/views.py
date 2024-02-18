from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

from bio.models import Bio
from search.query import text
from settings.models import Settings

# Create your views here.

@cache_page(0)
def search(request):

    query = request.GET.get('query')

    if query != '' and query != None:
        bios = Bio.objects.filter(text(query))
    else:
        return redirect('homepage')

    response = {
        "query": query,
        "bios": bios,
    }

    if not request.user.is_anonymous:
        response['settings'] = get_object_or_404(Settings, user=request.user)


    return render(request, "search.html", response)

