from django.db import models

# Create your models here.

class ComparisonDecision(models.Model):
    hand = models.CharField(max_length=255)
    bank_card = models.CharField(max_length=255)
    decision1 = models.CharField(max_length=255)
    decision2 = models.CharField(max_length=255)
    ev1 = models.FloatField()
    ev2 = models.FloatField()
    exp_decision = models.CharField(max_length=255)
    theoritical_decision = models.CharField(max_length=255)
    number_of_decks = models.IntegerField(default=6)
    number_of_simulations = models.BigIntegerField(default=10000000)
    class Meta:
        db_table = 'blackjack_comparison_decision'

    def __str__(self):
        return self.hand + ' VS ' + self.bank_card
    

class HandDecisionEV(models.Model):
    hand = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    bank_card = models.CharField(max_length=255)
    decision = models.CharField(max_length=255)
    ev = models.FloatField()
    number_of_decks = models.IntegerField(default=6)
    number_of_simulations = models.BigIntegerField(default=10000000)
    
    class Meta:
        db_table = 'blackjack_hand_decision_ev'

    def __str__(self):
        return self.hand + ' VS ' + self.bank_card
    
class ProbBankResults(models.Model):
    bank_card = models.CharField(max_length=255, blank=True, null=True)
    prob17 = models.FloatField()
    prob18 = models.FloatField()
    prob19 = models.FloatField()
    prob20 = models.FloatField()
    prob21 = models.FloatField()
    prob_bj = models.FloatField()
    prob_bust = models.FloatField()
    number_of_decks = models.IntegerField(default=6)
    number_of_simulations = models.BigIntegerField(default=10000000)
    
    class Meta:
        db_table = 'blackjack_prob_bank_result'