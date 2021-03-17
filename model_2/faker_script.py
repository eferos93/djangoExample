import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'model_2.settings')

import django

django.setup()  # sets up the project settings

from models_exercise.models import User
from faker import Faker

fakegen = Faker()


def add_user(name, surname, email):
    t = User.objects.get_or_create(first_name=name, last_name=surname, email=email)[0]
    t.save()
    # return t


def populate(n=10):
    for entry in range(n):
        add_user(fakegen.first_name(), fakegen.last_name(), fakegen.email())


if __name__ == '__main__':
    print('Populating script')
    populate(20)
    print('populating complete')
