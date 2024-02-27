from core.models import Restaurant, Sale, Rating, Staff
from django.utils import timezone
from pprint import pprint
from django.contrib.auth.models import User 
from django.db import connection
from django.db.models.functions import Lower
from django.db.models import Sum
from django.db.models import F
from django.db.models import Count, Avg, Min, Max, Sum
import random


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
    # _all = Restourant.objects.prefetch_related('ratings','sales') \
    # .filter(ratings__rating=5).annotate(total=Sum('sales__income'))
    # print(_all)
    # pprint(connection.queries)

    # querying many to many fields

    # lets first create a staff 
    # staff, created = Staff.objects.get_or_create(name='John Wick')
    #print(staff.restaurants.all())
    # you can remove 
    #staff.restaurants.remove(Restourant.objects.first())
    #staff.restaurants.add(Restourant.objects.first())
    #print(staff.restaurants.all())
    # to get the number of restaurants the staff works in 
    # we have seen methods like all, count, remove
    #print(staff.restaurants.count())

    # now we can you set method, this method will help you to override the existing row
    # staff.restaurants.set(Restourant.objects.all()[:10])
    # print(staff.restaurants.count())

    # you can also use filter to filter down 
    # italian = staff.restaurants.filter(restourant_type = Restourant.TypeChoices.ITALIAN)
    #print(italian)

    # you can do with other side as well, till this time we have done from the staff side
    # now you can do from the restaurant side and find the staff which works in restaurant


    # restaurant = Restourant.objects.get(pk=9)
    # print(restaurant.staff_set.all())

    # in some cases you might need to grab only one field not all of them,
    # then you can use other methods like 

    # restaurant = Restaurant.objects.values('name','date_opened').first()
    # print(restaurant)
    # pprint(connection.queries)

    # it is possible to grab foreign key value using values function
    # if you want to grab only italian restaurant with rating field. Note that 
    # restaurant field is the foreign key to Rating model

    # IT = Restaurant.TypeChoices.ITALIAN
    # ratings = Rating.objects.filter(restaurant__restaurant_type=IT).values('rating','restaurant__name')
    # print(ratings)

    # restaurants = Restaurant.objects.values_list('name',flat=True)
    # print(restaurants)

    # What aggregation does, it breaks down multiple values into single values
    # for instance we want to get back the number of restaurants 

    
    # restaurants = Restaurant.objects.aggregate(total=Count('id'))
    # print(restaurants)
    # print(connection.queries)

    # if we want to grab the average aggregation for rating 
    # rating = Rating.objects.aggregate(avg=Avg('rating'))
    # print(rating)
    # print(connection.queries)

    # if we want to grab min, max value for the particular column you can do

    # insight = Sale.objects.aggregate(
    #     _min = Min('income'),
    #     _max = Max('income'),
    #     _avg = Avg('income')
    # )
    #to grab the sales made in the past month you do
    # one_month_ago = timezone.now() - timezone.timedelta(days=31)
    # sales = Sale.objects.filter(datetime__gte=one_month_ago)
    # print(sales)

    # print(insight)

    # Difference between aggregation and annotation
    # When you annotate values you will get value added to each model in the queryset,
    # but aggregation will return single value

    # what if we want to annotate restaurants with the number of ratings
    # restaurants = Restaurant.objects.annotate(num_ratings = Count('ratings'))
    # print(restaurants.values('name','num_ratings'))

    # rating = Rating.objects.filter(rating=3).first()
    # rating.rating += 1
    # rating.save()
    # pprint(connection.queries)
    # in the example above we are pulling the value of rating and saving it to the
    # memory and adding one to the value which is stored in the memory

    # there is a better way, that is using F expressions
  
    # rating = Rating.objects.filter(rating=3).first()

    # rating.rating = F('rating') + 1 
    # rating.save()
    # pprint(connection.queries)

    # this way we are directly accessing the rating field and adding 1 to it
    
    # what if you want to change the rating system and instead use 1 to 10 rating
    # note that you have to update every single raw in the rating table 

    # Rating.objects.update(rating=F('rating') / 2)
    # pprint(connection.queries)


    sales = Sale.objects.all()
    for sale in sales:
        sale.expenditure = random.uniform(5,100)
    
    Sale.objects.bulk_update(sales, ['expenditure'])
    pprint(connection.queries)
    
    






    




    














    

    




    







    










    









