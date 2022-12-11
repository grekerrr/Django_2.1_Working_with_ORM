import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for phone in phones:
                # TODO: Добавьте сохранение модели
                # def create(self, phone_d):
                #     self.name = phone_d['name']
                #     self.price = float(phone_d['price'])
                #     self.image = phone_d['image']
                #     self.release_date = datetime.strptime(phone_d['release_date'], '%Y-%m-%d')
                #     self.lte_exists = bool(phone_d['lte_exists'])
                #     self.slug = phone_d['name']
                phone = Phone(name=phone['name'],
                              price=float(phone['price']),
                              image=phone['image'],
                              release_date=datetime.strptime(phone['release_date'], '%Y-%m-%d'),
                              lte_exists=bool(phone['lte_exists']))  # slug=phone['name'])
                phone.save()