from django import forms

from website.apps.blackjack.functions import order_hand
from website.apps.blackjack.models import ComparisonDecision, HandDecisionEV

class ComparisonDecisionForm(forms.ModelForm):
    class Meta:
        model = ComparisonDecision
        fields = '__all__'
        widgets = {
            'hand' : forms.TextInput(attrs={'size': 10}),
            'bank_card': forms.TextInput(attrs={'size': 10}),
            'decision1': forms.TextInput(attrs={'size': 10}),
            'decision2': forms.TextInput(attrs={'size': 10}),
            'ev1': forms.TextInput(attrs={'size': 10}),
            'ev2' : forms.TextInput(attrs={'size': 10}),
            'exp_decision': forms.TextInput(attrs={'size': 10}),
            'theoritical_decision': forms.TextInput(attrs={'size': 10}),
            'number_of_decks': forms.TextInput(attrs={'size': 10}),
            'number_of_simulations': forms.TextInput(attrs={'size': 10}),
        }

    def clean(self):
        cleaned_data = super(ComparisonDecisionForm, self).clean()
        cleaned_data['hand'] = order_hand(cleaned_data['hand'])
        return cleaned_data
        
class ComparisonDecisionAddForm(forms.ModelForm):
    class Meta:
        model = ComparisonDecision
        fields = ['hand', 'bank_card', 'decision1', 'decision2', 'number_of_decks', 'number_of_simulations']
        widgets = {
            'hand' : forms.TextInput(attrs={'size': 10}),
            'bank_card': forms.TextInput(attrs={'size': 10}),
            'decision1': forms.TextInput(attrs={'size': 10}),
            'decision2': forms.TextInput(attrs={'size': 10}),
            'number_of_decks': forms.TextInput(attrs={'size': 10}),
            'number_of_simulations': forms.TextInput(attrs={'size': 10}),
        }
        
    def clean(self):
        cleaned_data = super(ComparisonDecisionAddForm, self).clean()
        cleaned_data['hand'] = order_hand(cleaned_data['hand'])
        return cleaned_data
        
class HandDecisionEVForm(forms.ModelForm):
    class Meta:
        model = HandDecisionEV
        fields = ['hand', 'bank_card', 'decision', 'number_of_simulations']
        widgets = {
            'hand' : forms.TextInput(attrs={'size': 10}),
            'bank_card': forms.TextInput(attrs={'size': 10}),
            'decision': forms.TextInput(attrs={'size': 10}),
            'number_of_simulations': forms.TextInput(attrs={'size': 10}),
        }
        
    def clean(self):
        cleaned_data = super(HandDecisionEVForm, self).clean()
        cleaned_data['hand'] = order_hand(cleaned_data['hand'])
        return cleaned_data