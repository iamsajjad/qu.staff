from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from settings.models import Settings
from bio.models import Bio
from link.models import Link

from link.forms import LinkForm, DeleteLinkForm

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

        link = LinkForm(request.POST, instance=link)

        if link.is_valid():

            link.save()

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

