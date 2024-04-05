from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.shortcuts import redirect, render
from django.core.mail import send_mail

from django.contrib.auth.models import User
from django.conf import settings

from bio.models import Bio
from settings.models import Settings
from settings.forms import SettingsForm
from user.forms import UserRegisterForm

from user.slug import slug
from user.gen import PASSWORD

# Create your views here.

@cache_page(0)
def reset(request):

    # reset password and send the new password in email
    if request.method == 'POST':

        email = request.POST['email']
        user = User.objects.filter(email=email)

        if len(user) == 1:
            user = user[0]
        else:
            return redirect('signin')

        new_password = PASSWORD(12)
        user.set_password(new_password)
        user.save()

        # send the new password
        subject = 'Qadisiyah University | Academic Staff | Password reset'
        message = f'https://staff.qu.edu.iq\n\nYour Email : {user.email}\nThe new Password is : {new_password}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return redirect('signin')
    else:

        return render(request, 'user/reset.html')

    return redirect('/')

@cache_page(0)
def register(request):

    if request.method == 'POST':

        udpost = request.POST.copy()
        udpost['username'] = request.POST['email']
        request.POST = udpost

        user = UserRegisterForm(request.POST)

        if user.is_valid() and settings.IS_ORG_EMAIL(request.POST['email']):

            user = user.save(commit=False)
            user.is_superuser = False
            user.is_staff = False
            user.save()

            user_bio = Bio.objects.create(owner=user)

            user_settings = SettingsForm()
            user_settings = user_settings.save(commit=False)
            user_settings.user = user
            user_settings.slug = slug(user.email)
            user_settings.save()

            user_bio.slug = slug(user.email)
            user_bio.save()

            login(request, user)

            return redirect('biopage', user_settings.slug)
    else:

        return render(request, 'user/register.html')

    return redirect('/')


@cache_page(0)
def signin(request):

    if request.method == 'POST':

        username = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            if not Bio.objects.filter(owner=user).exists():

                # user is created using CLI with out bio object
                user_bio = Bio.objects.create(owner=user).save()

            if not Settings.objects.filter(user=user).exists():

                user_bio = Bio.objects.get(owner=user)

                # user is created using CLI with out settings object
                user_settings = SettingsForm().save(commit=False)
                user_settings.user = user
                user_settings.slug = slug(user.email)
                user_settings.save()

                user_bio.slug = slug(user.email)
                user_bio.save()

            login(request, user)

            user_settings = Settings.objects.get(user=user)

            return redirect('biopage', user_settings.slug)
        else:
            return redirect('signin')
    else:
        # get next page
        next_page = request.GET.get('next', '/')

        if User.objects.filter(username=request.user).exists():

            return redirect('/')

        response = {
            'next_page': next_page,
        }

    return render(request, 'user/signin.html', response)


@login_required
@cache_page(0)
def signout(request):

    logout(request)

    return redirect('homepage')

