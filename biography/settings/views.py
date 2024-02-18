from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.shortcuts import redirect, render
from django.contrib.auth import logout

from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

from settings.models import Settings
from settings.forms import SettingsForm
from user.forms import UserEditForm

# Create your views here.

@login_required
@cache_page(0)
def settings(request):

    settings = Settings.objects.get(user=request.user)

    if request.method == 'POST':
        user = UserEditForm(request.POST, instance=request.user)
        settings = SettingsForm(request.POST, request.FILES, instance=settings)

        if user.is_valid():
            user.save()

        if settings.is_valid():
            settings = settings.save(commit=False)

            if request.POST.get('mode', False):
                settings.mode = 'dark'
            else:
                settings.mode = 'light'

            settings.save()

            return redirect('settings')
    else:

        return render(request, 'settings/settings.html')

    return redirect('settings')

@login_required
@cache_page(0)
def password(request):

    user = User.objects.get(username=request.user.username)

    if request.method == 'POST':
        user = PasswordChangeForm(request.user, request.POST)

        if user.is_valid():

            user.save()

            logout(request)

    return redirect('settings')

