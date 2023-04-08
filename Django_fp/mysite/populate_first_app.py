#file to populate the database

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

#fake pop script

import random
from first_app.models import AccesRecord,Webpage,Topic
from faker import Faker

fakegen=Faker()
topics = ['Search', 'Social', 'Marketplace', 'Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate (N=5):
    for entry in range(N):

        #get the topic for the entry

        top = add_topic()

        #create fake data for rhat entry

        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        #create new web page entry

        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create a fake acces record
        acc_rec = AccesRecord.objects.get_or_create(name=webpg,date=fake_date)

if __name__ == '__main__':
    print('populate script!')
    populate(20)
    print('populating complete')