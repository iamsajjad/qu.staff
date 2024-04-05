
from bio.models import Bio
from link.models import Link
from publication.models import Publication

def status():
    return { 'bios':Bio.objects.count(),
             'links' : Link.objects.count(),
             'publications' : Publication.objects.count(),
            }

