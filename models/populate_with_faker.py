import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_model_app.settings')

import django
django.setup() # sets up the project settings

import random
from first_model_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0] # [0] bc it is the way it is formatted back
    # first element in the tuple is the object created
