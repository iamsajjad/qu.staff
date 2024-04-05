from random import sample

from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.http import HttpResponseRedirect
from django.utils import translation

from settings.models import Settings
from bio.models import Bio
from link.models import Link
from publication.models import Publication

# Create your views here.

# @cache_page(0)
def homepage(request):

    response = {}

    # Fetch the IDs of all objects
    bios_pks = Bio.objects.values_list('pk', flat=True)

    if bios_pks.count() <= 10:
        bios = Bio.objects.all()
    else:
        # Get 10 random IDs
        random_bios_pks = sample(list(bios_pks), 10)
        # Fetch the objects corresponding to these IDs
        bios = Bio.objects.filter(pk__in=random_bios_pks)

    response = {
        'bios': bios,
    }

    if not request.user.is_anonymous:
        response['settings'] = get_object_or_404(Settings, user=request.user)

        # footer status informations
        response['status'] = {'bios': Bio.objects.count(),
                              'links': Link.objects.count(),
                              'publications': Publication.objects.count(),
        }

    return render(request, 'home.html', response)

# @cache_page(0)
def language(request, pagepath):

    if pagepath.startswith('/en/'):
        pagepath = pagepath.replace('en', 'ar', 1)
        return HttpResponseRedirect(pagepath)
    elif pagepath.startswith('/ar/'):
        pagepath = pagepath.replace('ar', 'en', 1)
        return HttpResponseRedirect(pagepath)
    else:
        return HttpResponseRedirect('/en/')

def notfound(request):

    response = {}

    return render(request, 'error/notfound.html', response)

