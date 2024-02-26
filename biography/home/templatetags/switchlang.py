from django import template

register = template.Library()

@register.filter
def switchlang(pagepath):
    if pagepath.startswith('/en/'):
        return pagepath.replace('en', 'ar', 1)
    elif pagepath.startswith('/ar/'):
        return pagepath.replace('ar', 'en', 1)
    else:
        return '/en/'

