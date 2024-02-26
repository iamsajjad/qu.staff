from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from settings.models import Settings
from bio.models import Bio
from link.models import Link

from link.forms import LinkForm, EditLinkForm, DeleteLinkForm

from link.const import REQUIREDSITES

# Create your views here.

@login_required
def new(request, slug):

    settings = get_object_or_404(Settings, slug=slug)
    bio = Bio.objects.get(owner=settings.user)

    # to edit bio the user must be `superuser` or `owner`
    authorized = request.user.is_superuser or request.user == bio.owner

    if request.method == 'POST' and authorized:

        link = LinkForm(request.POST)

        if link.is_valid():

            if REQUIREDSITES.get(request.POST['name'], False) == False:
                # unknown url name
                return redirect('edit', slug=settings.slug)

            urlprefix = REQUIREDSITES[request.POST['name']]

            if not request.POST['url'].startswith(urlprefix):
                # url and url name not match
                return redirect('edit', slug=settings.slug)

            if len(request.POST['url']) <= len(urlprefix):
                # if given url is matching only the website prefix
                return redirect('edit', slug=settings.slug)

            link = link.save()

            bio.links.add(link)
            bio.save()

    return redirect('edit', slug=settings.slug)

@login_required
def edit(request, slug, linkid):

    settings = get_object_or_404(Settings, slug=slug)
    bio = Bio.objects.get(owner=settings.user)
    link = Link.objects.get(id=linkid)

    # to edit bio the user must be `superuser` or `owner`
    authorized = request.user.is_superuser or request.user == bio.owner

    if request.method == 'POST' and authorized:

        editlink = EditLinkForm(request.POST, instance=link)

        if editlink.is_valid():

            urlprefix = REQUIREDSITES[link.name]

            if not request.POST['url'].startswith(urlprefix):
                # url and url name not match
                return redirect('edit', slug=settings.slug)

            if len(request.POST['url']) <= len(urlprefix):
                # if given url is matching only the website prefix
                return redirect('edit', slug=settings.slug)

            editlink.save()

    return redirect('edit', slug=settings.slug)

@login_required
def delete(request, slug, linkid):

    settings = get_object_or_404(Settings, slug=slug)
    bio = Bio.objects.get(owner=settings.user)
    link = Link.objects.get(id=linkid)

    # to edit bio the user must be `superuser` or `owner`
    authorized = request.user.is_superuser or request.user == bio.owner

    if request.method == 'POST' and authorized:

        form = DeleteLinkForm(request.POST, instance=link)

        if form.is_valid():

            link.delete()

    return redirect('edit', slug=settings.slug)

