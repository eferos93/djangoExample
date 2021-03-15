import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'models.settings')

import django

django.setup()  # sets up the project settings

import random
from first_model_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]  # [0] bc it is the way it is formatted back
    # first element in the tuple is the object created
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        # get the topic for the entry
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create webpage entry
        webpage = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # crate a face access record
        access_record = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)


if __name__ == '__main__':
        print('Populating script')
        populate(20)
        print('populating complete')
