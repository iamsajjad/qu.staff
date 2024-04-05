from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.contrib.auth import logout

from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

from settings.models import Settings
from bio.models import Bio
from publication.models import Publication
from link.models import Link

from settings.forms import SettingsForm
from user.forms import UserEditForm

# Create your views here.

@login_required
@cache_page(0)
def settings(request):

    response = {
        'settings': get_object_or_404(Settings, user=request.user),
        # footer status informations
        'status': {'bios': Bio.objects.count(),
                   'links': Link.objects.count(),
                   'publications': Publication.objects.count(),
                   },
    }

    return render(request, 'settings.html', response)

@login_required
@cache_page(0)
def password(request):

    user = User.objects.get(username=request.user.username)

    if request.method == 'POST':
        passwordform = PasswordChangeForm(request.user, request.POST)

        if passwordform.is_valid():

            passwordform.save()

            logout(request)

    return redirect('settings')

