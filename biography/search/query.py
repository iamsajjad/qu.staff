
from functools import lru_cache

from django.db.models import Q


@lru_cache(maxsize=512)
def text(query):

    return Q(
        Q(full_name__icontains=query) |
        Q(surname__icontains=query) |
        Q(nationality__icontains=query) |
        Q(gender__icontains=query) |
        Q(degree__icontains=query) |
        Q(academic_title__icontains=query) |
        Q(college__icontains=query) |
        Q(department__icontains=query) |
        Q(major__icontains=query) |
        Q(specialty__icontains=query) |
        Q(position__icontains=query) |
        Q(occupation__icontains=query) |
        Q(mother_lang__icontains=query) |
        Q(other_langs__icontains=query) |
        Q(personal_email__icontains=query) |
        Q(work_email__icontains=query) |
        Q(ar_full_name__icontains=query) |
        Q(ar_nationality__icontains=query) |
        Q(ar_academic_title__icontains=query) |
        Q(ar_college__icontains=query) |
        Q(ar_department__icontains=query) |
        Q(ar_major__icontains=query) |
        Q(ar_specialty__icontains=query) |
        Q(ar_position__icontains=query) |
        Q(ar_occupation__icontains=query) |
        Q(ar_mother_lang__icontains=query) |
        Q(ar_other_langs__icontains=query) |
        Q(ar_state__icontains=query) |
        Q(ar_district__icontains=query) |
        Q(slug__icontains=query)
    )

