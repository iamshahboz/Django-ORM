from core.models import Restourant, Sale
from django.utils import timezone
def run():
    
    restaurant = Restourant()
    restaurant.name = 'My Italian Restaurant'
    restaurant.latitude = 50.2
    restaurant.longitude = 40.5
    restaurant.date_opened = timezone.now()
    restaurant.restourant_type = Restourant.TypeChoices.ITALIAN
    restaurant.save()
    

