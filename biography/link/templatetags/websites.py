
from django import template

from link.const import REQUIREDSITES

register = template.Library()

@register.filter
def websites(userlinks):

    needed = []

    names = [ul.name for ul in userlinks]
    for name in REQUIREDSITES.keys():
        if name not in names and name != 'Website':
            needed.append(name)

    needed.append('Website')

    return needed

@register.filter
def sortsites(userlinks):

    sortedlinks = []

    for name in REQUIREDSITES.keys():
        usersite = userlinks.filter(name=name)
        if usersite:
            sortedlinks.extend(i for i in usersite)

    return sortedlinks

@register.filter
def isdone(userlinks):

    needed = []

    names = [ul.name for ul in userlinks]
    for name in REQUIREDSITES.keys():
        if name not in names:
            needed.append(name)

    if needed == [] or needed == ['Website']:
        return True
    return False

@register.filter
def neededonly(userlinks):

    needed = []

    for ul in userlinks:
        if ul.name in REQUIREDSITES.keys() and ul.name != 'Website':
            needed.append(ul)

    return needed

