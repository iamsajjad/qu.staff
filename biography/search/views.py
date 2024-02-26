from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.db.models import Q

from bio.models import Bio
from link.models import Link
from publication.models import Publication
from settings.models import Settings

from search.query import text

# Create your views here.

# @cache_page(0)
def search(request):

    query = request.GET.get('query')

    if query != '' and query != None:
        bios = Bio.objects.filter(text(query))
    else:
        return redirect('homepage')

    response = {
        'query': query,
        'bios': bios,
    }

    if not request.user.is_anonymous:
        response['settings'] = get_object_or_404(Settings, user=request.user)

        # footer status informations
        response['status'] = {'bios':Bio.objects.count(),
                              'links' : Link.objects.count(),
                              'publications' : Publication.objects.count(),
        }

    return render(request, 'search.html', response)

def getstaff(request):

    if request.LANGUAGE_CODE == 'en':
        college = request.POST.get('college')
        academic_title = request.POST.get('academic_title')
        bios = Bio.objects.filter(Q(college=college) & Q(academic_title=academic_title))
        response = {
            'college': college,
            'academic_title': academic_title,
            'staffquery': f'{college} | {academic_title}',
            'bios': bios,
        }

    else:
        ar_college = request.POST.get('ar_college')
        ar_academic_title = request.POST.get('ar_academic_title')
        bios = Bio.objects.filter(Q(ar_college=ar_college) & Q(ar_academic_title=ar_academic_title))

        response = {
            'ar_college': ar_college,
            'ar_academic_title': ar_academic_title,
            'staffquery': f'{ar_academic_title} | {ar_college}',
            'bios': bios,
        }

    if not request.user.is_anonymous:
        response['settings'] = get_object_or_404(Settings, user=request.user)

        # footer status informations
        response['status'] = {'bios':Bio.objects.count(),
                              'links' : Link.objects.count(),
                              'publications' : Publication.objects.count(),
        }

    return render(request, 'search.html', response)

