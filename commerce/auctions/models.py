from django.contrib.auth.models import AbstractUser
from django.db import models

# each modify in models.py, you’ll need to first
# run python manage.py makemigrations
#and then
# python manage.py migrate
#to migrate those changes to your database.


#Django Models are a level of abstraction on top of SQL that allow us to work with databases
#using Python classes and objects rather than direct SQL queries.

class User(AbstractUser):
    first = models.CharField(max_length=61)
    last = models.CharField(max_length=52)
    highlists = models.ManyToManyField(Highlist, blank=True, related_name="passengers") #they can be in multiple flights

    def __str__(self):
        return f"{self.first} {self.last}"


class Highlist(models.Model):
# listagem leilao
     title = models.CharField(max_length=64)
     hightext  = models.CharField(max_length=64)
     imageurl =  models.CharField(max_length=64) #configure
     base = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="hashtag")
     price  = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"


class Category(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=64)

class Bids:
# lances
    pass

class CommentsAuctionList:
#comentarios nas listagens
    pass
