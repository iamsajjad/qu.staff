from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.shortcuts import render

from django.core.paginator import Paginator

from history.models import Log

# Create your views here.

@login_required
@cache_page(0)
def history(request):

    logs = Log.objects.filter(user=request.user).order_by('-id')

    paginator = Paginator(logs, 100)
    page = request.GET.get('page')
    logs = paginator.get_page(page)

    response = {
        'logs': logs,
    }

    return render(request, 'history/history.html', response)

