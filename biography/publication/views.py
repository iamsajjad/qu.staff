
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from settings.models import Settings
from bio.models import Bio
from publication.models import Publication

from publication.forms import PublicationForm, DeletePublicationForm

# Create your views here.

@login_required
def new(request, slug):

    settings = get_object_or_404(Settings, slug=slug)
    bio = Bio.objects.get(owner=settings.user)

    # to edit bio the user must be `superuser` or `owner`
    authorized = request.user.is_superuser or request.user == bio.owner

    if request.method == 'POST' and authorized:

        publication = PublicationForm(request.POST)

        if publication.is_valid():

            publication = publication.save()

            bio.publications.add(publication)
            bio.save()
        else:
            print(publication.errors)

    return redirect('edit', slug=settings.slug)

@login_required
def edit(request, slug, pubid):

    settings = get_object_or_404(Settings, slug=slug)
    bio = Bio.objects.get(owner=settings.user)
    publication = Publication.objects.get(id=pubid)

    # to edit bio the user must be `superuser` or `owner`
    authorized = request.user.is_superuser or request.user == bio.owner

    if request.method == 'POST' and authorized:

        publication = PublicationForm(request.POST, instance=publication)

        if publication.is_valid():

            publication.save()

    return redirect('edit', slug=settings.slug)

@login_required
def delete(request, slug, pubid):

    settings = get_object_or_404(Settings, slug=slug)
    bio = Bio.objects.get(owner=settings.user)
    publication = Publication.objects.get(id=pubid)

    # to edit bio the user must be `superuser` or `owner`
    authorized = request.user.is_superuser or request.user == bio.owner

    if request.method == 'POST' and authorized:

        form = DeletePublicationForm(request.POST, instance=publication)

        if form.is_valid():

            publication.delete()

    return redirect('edit', slug=settings.slug)

