import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'models.settings')

import django

django.setup()  # sets up the project settings

from models_exercise.models import User
from faker import Faker

fakegen = Faker()


def add_user():
    t = User.objects.get_or_create()[0]
    t.save()
    return t


def populate(n=10):
    for entry in range(n):
        user = add_user()
        user.first_name = fakegen.name()
        user.last_name = fakegen.last_name()
        user.email = fakegen.email()


if __name__ == '__main__':
    print('Populating script')
    populate(20)
    print('populating complete')
