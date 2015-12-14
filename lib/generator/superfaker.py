from faker import Factory
import random


class SuperFaker(object):
    faker = None
    locale = 'it_IT'

    def __init__(self, locale='it_IT'):
        self.faker = Factory.create(locale)
        self.locale = locale

    def name(self):
        name = self.faker.name_male().split()

        if len(name) == 3:
            name = name[1]
        else:
            name = name[0]
        if self.locale == 'it_IT' and name[-1] == 'a':
            name = name[:-1] + 'o'
        return name

    def surname(self):
        return self.faker.last_name()

    def age(self, mn=16, mx=38):
        return random.randint(mn, mx)
