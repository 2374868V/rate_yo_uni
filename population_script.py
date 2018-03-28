import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','rate_yo_uni.settings')

import django
django.setup()

from project.models import Bathroom

def populate():

    #data
    bathrooms = [
        {"building": 'Boyd Orr',
         "level": '1',
         "gender": 'female'
        },
        {"building":'Queen Margaret Union',
         "level": '1',
         "gender": 'male'
        },
        {"building": 'Queen Margaret Union',
         "level":'3',
         "gender": 'neutral'
        },
        {"building":'Sir Charles Wilson',
         "level": '1',
         "gender": 'female'
        },
        {"building": 'Boyd Orr',
         "level": '6',
         "gender": 'female'
        },
        {"building": 'Boyd Orr',
         "level": '7',
         "gender": 'male'
        },
        {"building": 'University Library',
         "level": '2',
         "gender": 'neutral'
        },
        {"building": 'Main Building',
         "level": '2',
         "gender": 'female'
        },
    ]

    for bat in bathrooms:
        add_bathroom(bat["building"], bat["level"], bat["gender"])

def add_bathroom(building, level, gender):
    name = building + " " + level + " " + gender
    b = Bathroom.objects.get_or_create(name=name, building=building, level=level, gender=gender)[0]
    b.save()
    return b

if __name__ == '__main__':
    print('Starting population...')
    populate()