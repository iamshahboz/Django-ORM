from core.models import Restourant, Sale, Rating
from django.utils import timezone
from pprint import pprint
from django.contrib.auth.models import User 
from django.db import connection
def run():
    
    # in order to create a record you do like this

    # restaurant = Restourant()
    # restaurant.name = 'My Italian Restaurant'
    # restaurant.latitude = 50.2
    # restaurant.longitude = 40.5
    # restaurant.date_opened = timezone.now()
    # restaurant.restourant_type = Restourant.TypeChoices.ITALIAN
    # restaurant.save()

    # to pull out the records you do 

    # restaurant = Restourant.objects.all()
    # print(restaurant)
    #print(connection.queries)

    # the second way to create objects in Django 
    # Restourant.objects.create(
    #     name='Pizza shop',
    #     date_opened = timezone.now(),
    #     restourant_type = Restourant.TypeChoices.ITALIAN,
    #     latitude = 30.8,
    #     longitude = 22.3 
    # )
    # print(connection.queries)

    # to get the count of restaurants you can do 
    # print(Restourant.objects.count())
    # print(connection.queries)

    # we have also last method, first method

    # quering foreign key objects
    # restaurant = Restourant.objects.first()
    # user = User.objects.first()
    # Rating.objects.create(user=user,restaurant=restaurant,rating=3)
    
    # filtering
    # print(Rating.objects.filter(rating=3))
    # print(connection.queries)

    #print(Rating.objects.filter(rating=5))

    # query lookup
    # print(Rating.objects.filter(rating__gte=3))
    # print(connection.queries)

    # we have exclude, when we use it the condition which is passed to that 
    # function is actually what is not brought back from the database

    # updating queries
    # restaurant = Restourant.objects.first()
    # print(restaurant.name)

    # restaurant.name = 'ahahahah'
    # restaurant.save()
    # pprint(connection.queries)

    # accessing foreign key child object from parent object
    # restaurant = Restourant.objects.first()
    
    # this will return all the ratings of the first restaurant
    #print(restaurant.rating_set.all())

    # after adding related name we can access with the related name keyword

    # print(restaurant.ratings.all())

    # creating object instance 
    # Sale.objects.create(
    #     restaurant = Restourant.objects.first(),
    #     income = 2.33,
    #     datetime  = timezone.now()
    # )
    # Sale.objects.create(
    #     restaurant = Restourant.objects.first(),
    #     income = 8.20,
    #     datetime  = timezone.now()
    # )

    # restaurants = Restourant.objects.first()
    # print(restaurants.sales.all())

    # get or create method 
    # user = User.objects.first()
    # restaurant  = Restourant.objects.first()

    # print(Rating.objects.get_or_create(
    #     restaurant = restaurant,
    #     user = user,
    #     rating = 4

    # ))
    # pprint(connection.queries)


    # since it returns tuple you can assign it to a variable and do some logic 

    # rating, created = Rating.objects.get_or_create(
    #     restaurant = restaurant,
    #     user = user,
    #     rating=4
    # )

    # logic might be 
        #if created:
        # send email message
    
    # updating instance after overriding save method in the models

    # restaurant = Restourant()
    # restaurant.name = 'My Italian Restaurant #2'
    # restaurant.date_opened = timezone.now()
    # restaurant.restourant_type = Restourant.TypeChoices.ITALIAN
    # restaurant.latitude = 44.9
    # restaurant.longitude = 30.9
    # restaurant.save()

    # what if we want to update the date opened field for all of the records in the database

    # restaurant = Restourant.objects.all()
    # restaurant.update(
    #     date_opened = timezone.now()
        
    # )

    # print(connection.queries)

    # restaurants = Restourant.objects.filter(name__startswith='P')
    # print(restaurants)

    # print(restaurants.update(
    #     date_opened = timezone.now()-timezone.timedelta(days=365),
    #     website = 'https://home.tj'

    # ))
    # print(connection.queries)

    # deleting rows and querysets
    # restaurant = Restourant.objects.first()
    # print(restaurant.delete())
    # print(connection.queries)

    # if you want to delete all of the records you can do 

    # Restourant.objects.all().delete()
    # print(connection.queries)






    









