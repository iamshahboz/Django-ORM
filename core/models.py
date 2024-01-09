from django.db import models
from django.contrib.auth.models import User 
from django.db.models.functions import Lower
from django.core.validators import MinValueValidator, MaxValueValidator


# Restaurant
# User
# Rating 

class Restourant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fast Food'
        OTHER = 'OT', 'Other'


    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    restourant_type = models.CharField(max_length=5, choices = TypeChoices.choices)

    # this method helps whenever this model is called using ORM it will set the ordering to name
    
    class Meta:
        ordering = [Lower('name')]


    def __str__(self):
        return self.name 
    
    def save(self,*args,**kwargs):
        print(self._state.adding)
        super().save(*args,**kwargs)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    restaurant = models.ForeignKey(Restourant, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )

    def __str__(self):
        return f'Rating: {self.rating}'
    
class Sale(models.Model):
    restaurant = models.ForeignKey(Restourant, on_delete = models.SET_NULL, null=True,blank=True, related_name='sales')
    income = models.DecimalField(max_digits=8,decimal_places=2)
    datetime = models.DateTimeField()
    

