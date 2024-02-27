from django.db import models
from django.contrib.auth.models import User 
from django.db.models.functions import Lower
from django.core.validators import MinValueValidator, MaxValueValidator


# Restaurant
# User
# Rating 
# Staff 



class Restaurant(models.Model):
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
    restaurant_type = models.CharField(max_length=5, choices = TypeChoices.choices)

    # this method helps whenever this model is called using ORM it will set the ordering to name
    
    class Meta:
        ordering = [Lower('name')]


    def __str__(self):
        return self.name 
    
    def save(self,*args,**kwargs):
        print(self._state.adding)
        super().save(*args,**kwargs)

class Staff(models.Model):
    name = models.CharField(max_length=50)
    restaurants = models.ManyToManyField(Restaurant, through='StaffRestaurant')

    def __str__(self):
        return self.name
    
class StaffRestaurant(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    salary = models.FloatField(null=True)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )

    def __str__(self):
        return f'Rating: {self.rating}'
    
class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete = models.SET_NULL, null=True,blank=True, related_name='sales')
    income = models.DecimalField(max_digits=8,decimal_places=2)
    expenditure = models.DecimalField(max_digits=8,decimal_places=2)
    datetime = models.DateTimeField()

# in order to show many to many relationship we can add one more model which is Staff
# assuming that one staff can work for several restaurants at the same time 
# and also one restaurant will require many staff
# after implementing many to many relationship, django adds junction table 
    

    

