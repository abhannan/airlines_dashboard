from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Airline, Year, FinancialData

@receiver(post_save, sender=Airline)
def airline_selection_handler(sender, **kwargs):
	print("Initiated")

