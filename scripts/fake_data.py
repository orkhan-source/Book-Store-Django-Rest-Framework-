from rest_framework import serializers
from rest_framework.serializers import Serializer
from books.api.serializers import BookSerializer
from pprint import pprint
import requests
import django
from faker import Faker
from django.contrib.auth.models import User

import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_store.settings')

django.setup()


def set_user():
    fake = Faker(['en_US'])

    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f'{f_name.lower()}_{l_name.lower()}'
    email = f'{u_name}@{fake.domain_name()}'
    print(f_name, l_name, email)

    user_check = User.objects.filter(username=u_name)

    while user_check.exists():
        u_name = u_name + str(random.randrange(1, 99))
        user_check = User.objects.filter(username=u_name)

    user = User(username=u_name, first_name=f_name,
                last_name=l_name, email=email)

    user.save('tesing321..')
    user.save()


def book_add(topic):
    fake = Faker(['en_US'])
    url = 'https://openlibrary.org/search.json'
    payload = {'q': topic}
    response = requests.get(url, params=payload)

    if response.status_code != 200:
        print('Wrong request!', response.status_code)
        return
    jsn = response.json()

    books = jsn.get('docs')
    for book in books:
        book_name = book.get('title')
        data = {
            'name': book_name,
            'author': book.get('author_name')[0],
            'preface': f'{fake.paragraphs(nb=1)}',
            'publication_date': fake.date_time_between(start_date='-10y', end_date='now', tzinfo=None)
        }

        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("Saved", book_name)
        else:
            continue
