from django import template

from website.apps.blackjack.models import HandDecisionEV


register = template.Library()

@register.filter(name='dictvalue')
def dictvalue(dict, arg):
    try:
        return dict[arg]
    except:
        return None

# filter for number of decks = 6
@register.filter(name='hands_list_from_key')
def hands_list_from_key(key, decision):
    objs = HandDecisionEV.objects.filter(key=key, number_of_decks=6, decision=decision).order_by('hand').distinct('hand')
    if not objs:
        return ['-']
    return list(objs.values_list('hand', flat=True))

@register.filter(name='get_ev_stand')
def get_ev_stand(hand, card):
    obj = HandDecisionEV.objects.filter(hand=hand, number_of_decks=6, bank_card=card, decision='-')
    if not obj:
        return '-'
    return str(round(obj.first().ev,2)) + '%'

@register.filter(name='get_ev_hit')
def get_ev_hit(hand, card):
    obj = HandDecisionEV.objects.filter(hand=hand, number_of_decks=6, bank_card=card, decision='H')
    if not obj:
        return '-'
    return str(round(obj.first().ev,2)) + '%'

@register.filter(name='get_ev_double')
def get_ev_double(hand, card):
    obj = HandDecisionEV.objects.filter(hand=hand, number_of_decks=6, bank_card=card, decision='D')
    if not obj:
        return '-'
    return str(round(obj.first().ev,2)) + '%'

@register.filter(name='get_ev_split')
def get_ev_split(hand, card):
    obj = HandDecisionEV.objects.filter(hand=hand, number_of_decks=6, bank_card=card, decision='S')
    if not obj:
        return '-'
    return str(round(obj.first().ev,2)) + '%'