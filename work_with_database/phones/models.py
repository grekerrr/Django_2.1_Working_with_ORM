from datetime import datetime

from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.CharField(max_length=250)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.price}: {self.release_date}'

    def create(self, phone):
        self.name = phone['name']
        self.image = phone['image']
        self.price = float(phone['price'])
        self.release_date = datetime.strptime(phone['release_date'], '%Y-%m-%d')
        self.lte_exists = bool(phone['lte_exists'])
        self.slug = phone['name']