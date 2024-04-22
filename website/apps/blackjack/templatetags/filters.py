from django import template


register = template.Library()

@register.filter(name='dictvalue')
def dictvalue(dict, arg):
    try:
        return dict[arg]
    except:
        return None