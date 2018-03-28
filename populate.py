import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rate_yo_uni.settings')

import django
django.setup()

from project.models import *


def make_name(b, l, g):
    n = ""
    for i in b.__str__().split():
        n = n + i.capitalize()[0]
    n = n + l.__str__() + g.__str__()
    return n


def make_image_name(n, b):
    return b.__str__() + "-" + n


def populate():

    bathrooms = [
        {"building": 'Boyd Orr',
         "level": '2',
         "gender": 'F'
         },
        {"building": 'Queen Margaret Union',
         "level": '1',
         "gender": 'M'
         },
        {"building": 'Queen Margaret Union',
         "level": '3',
         "gender": 'N'
         },
        {"building": 'Sir Charles Wilson',
         "level": '1',
         "gender": 'F'
         },
        {"building": 'Boyd Orr',
         "level": '6',
         "gender": 'F'
         },
        {"building": 'Boyd Orr',
         "level": '7',
         "gender": 'M'
         },
        {"building": 'University Library',
         "level": '2',
         "gender": 'N'
         },
        {"building": 'Main Building',
         "level": '2',
         "gender": 'F'
         },
        {"building": 'Boyd Orr',
         "level": '2',
         "gender": 'M'
         },
        {"building": 'Glasgow University Union',
         "level": 1,
         "gender": 'M'
        }
    ]

    users = [
        {"user": 'user0',
         "password": 'qwer12340'
        },
        {"user": 'user1',
         "password": 'qwer12341'
         },
        {"user": 'user2',
         "password": 'qwer12342'
         },
        {"user": 'user3',
         "password": 'qwer12343'
         },
        {"user": 'user4',
         "password": 'qwer12344'
         },
        {"user": 'user5',
         "password": 'qwer12345'
         },
        {"user": 'user6',
         "password": 'qwer12346'
         },
        {"user": 'user7',
         "password": 'qwer12347'
         },
        {"user": 'user8',
         "password": 'qwer12348'
        },
        {"user": 'user9',
         "password": 'qwer12349'
         },

    ]

    ratings = [
        {"rating": 4,
         "User": 'user9'
         },
        {"rating": 5,
         "User": 'user5'
         },
        {"rating": 2,
         "User": 'user7'
         },
        {"rating": 4,
         "User": 'user3'
         },
        {"rating": 1,
         "User": 'user5'
         },
        {"rating": 1,
         "User": 'user6'
         },
        {"rating": 4,
         "User": 'user2'
         },
        {"rating": 3,
         "User": 'user0'
         },
    ]

    comments = [
        {"comment": 'It is okay',
         "User": 'user0'
         },
        {"comment": 'It is okay',
         "User": 'user1'
         },
        {"comment": 'It is okay',
         "User": 'user3'
         },
        {"comment": 'It is okay',
         "User": 'user4'
         },
        {"comment": 'It is okay',
         "User": 'user5'
         },
        {"comment": 'It is okay',
         "User": 'user8'
         },
        {"comment": 'It is okay',
         "User": 'user9'
         },
    ]

    images = [
        {"image": 'https://secure.i.telegraph.co.uk/multimedia/archive/03061/toilets_3061318b.jpg',
         "name": '1'
        },
        {"image": 'http://www.wallerservices.com/wp-content/uploads/2015/06/Langtons-2-Copy-Custom.jpg',
         "name": '2'
        },
        {"image": 'http://www.paradigminteriors.co.uk/userfiles/pages/fe5ba38551ea4149222347dc91095978_Sea_toilet_refurb_sinks_2.jpg',
         "name": '3'
        }
    ]

    for bat in bathrooms:
        add_bathroom(bat["building"], bat["level"], bat["gender"])

    for us in users:
        add_user(us["user"], us["password"])

    for b in Bathroom.objects.all()[0:3]:
        for i in images:
            imName = make_image_name(i["name"], b.b_slug)
            add_image(i["image"], imName, b)
        for c in comments:
            user = UserProfile.objects.get(user__username=c["User"])
            add_comment(c["comment"], user, b)
        for r in ratings:
            user = UserProfile.objects.get(user__username=r["User"])
            add_rating(r["rating"], user, b)


def add_bathroom(building, level, gender):
    name = make_name(building, level, gender)
    b = Bathroom.objects.get_or_create(name=name, building=building, level=level, gender=gender)[0]
    b.b_slug = b.name.lower()
    b.save()


def add_image(i, name, b):
    im = BathroomImages.objects.get_or_create(name=name, bathroom=b)[0]
    im.save()


def add_user(u, p):
    use = User.objects.get_or_create(username=u)[0]
    use.set_password(p)
    use.save()
    uProfile = UserProfile.objects.get_or_create(user=use)[0]
    uProfile.website = "www.google.co.uk"
    uProfile.save()


def add_comment(c, u, b):
    com = Comment.objects.get_or_create(bathroom=b, user=u, comment=c)[0]
    com.save()


def add_rating(r, u, b):
    rate = Rate.objects.get_or_create(bathroom=b, user=u, rating=r)[0]
    rate.save()


if __name__ == '__main__':
    print('Starting population...')
    populate()
