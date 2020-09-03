from django.db import models
from . import util


class Product (models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(null=True)
    util.save_entry(title,"teste")

    def __str__(self):
        return self.title
