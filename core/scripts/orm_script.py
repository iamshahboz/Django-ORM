from core.models import Restourant, Sale, Rating
from django.utils import timezone
from pprint import pprint
from django.contrib.auth.models import User 
from django.db import connection
from django.db.models.functions import Lower
from django.db.models import Sum


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

    # filter down to only Chinese restaurant
    # chinese = Restourant.objects.filter(restourant_type=Restourant.TypeChoices.CHINESE)
    # pprint(chinese)
    # print(connection.queries)

    # passing multiple choices

    # chinese = Restourant.TypeChoices.CHINESE
    # restaurants = Restourant.objects.filter(restourant_type = chinese, name__startswith='C')
    # print(restaurants)
    # print(connection.queries)

    # filtering using in filter

    # chinese = Restourant.TypeChoices.CHINESE
    # indian = Restourant.TypeChoices.INDIAN
    # mexican = Restourant.TypeChoices.MEXICAN
    # check_types = [chinese,indian,mexican]

    # restaurants = Restourant.objects.filter(restourant_type__in=check_types)
    # pprint(restaurants)
    # print(connection.queries)

    # you can use exclude method which allows you to handle not in scenerio

    # chinese = Restourant.TypeChoices.CHINESE
    # restaurants = Restourant.objects.exclude(restourant_type=chinese)
    # print(restaurants)
    # pprint(connection.queries)

    # now lets get back all the list of restaurants which the name 
    # starts with A, B, C, D

    # restaurants = Restourant.objects.filter(name__lt='E')
    # print(restaurants)
    # print(connection.queries)

    # get the sales greater than specific value

    # sale = Sale.objects.filter(income__gt=90)
    # print(sale)
    # print(connection.queries)

    # range 
    # sales = Sale.objects.filter(income__range=(40,60))
    # print(sales)
    # print([sale.income for sale in sales])
    # print(connection.queries)

    # we can also order by the returned query

    # now the problem is that it is case sensitive
    # restaurants = Restourant.objects.order_by('name').reverse()
    # print(restaurants)

    # print(connection.queries)

    # in order to handle the issue we can import the build in funciton

    # restaurants = Restourant.objects.order_by(Lower('name')).reverse()
    # print(restaurants)

    # print(connection.queries)

    # we can limit 
    # restaurants = Restourant.objects.all()
    # print(restaurants)
    # print(connection.queries)


    # earliest is for datetime
    # latest is also for datetime. They are not a queryset, but single row 


    # filtering foreign key

    # ratings = Rating.objects.filter(restaurant__name__startswith='C')
    # print(ratings)
    # print(connection.queries)

    # now we passed exclude function. What it does, it says that give me back 
    # all the restaurans back which does not match the condition we pass 
    # chinese = Restourant.TypeChoices.CHINESE

    # restaurants = Restourant.objects.exclude(restourant_type=chinese)
    # print(restaurants)
    # pprint(connection.queries)

    
    # we can get the boundaries of the income by using range

    # sales = Sale.objects.filter(income__range=(50, 60))
    # print([sale.income for sale in sales])
    # pprint(connection.queries)

    # the better use case of range will be datetime

    # When you use Django ORM you can face N+1 problem based on how you write code
    # in order to get all of the rating accosiated to each restaurant you can do
    # ratings = Restourant.objects.prefetch_related('ratings','sales')
    # print(ratings)
    # pprint(connection.queries)

    # if we want to fetch only the restaurants whose name starts with latter c
    # ratings = Restourant.objects.filter(name__istartswith='c').prefetch_related('ratings')
    # print(ratings)
    # pprint(connection.queries)

    # now we want to grab the ratings and as you know each rating is bound to a restaurant
    # which is foreign key relationship

    # don't do
    # rating = Rating.objects.all()
    # print(rating)
    # pprint(connection.queries)

    # do 
    # ratings = Rating.objects.select_related('restaurant')
    # print(ratings)
    # pprint(connection.queries)

    # get all 5 star ratings and fetch all the sales for restaurants with 5 star rating
    _all = Restourant.objects.prefetch_related('ratings','sales') \
    .filter(ratings__rating=5).annotate(total=Sum('sales__income'))
    print(_all)
    pprint(connection.queries)





    

    




    







    










    









