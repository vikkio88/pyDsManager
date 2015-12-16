class Person(object):
    name = ""
    surname = ""
    nationality = ""
    age = 0
    skill = 0

    def __str__(self, *args, **kwargs):
        return "{} {}, ({}) - {}".format(self.name, self.surname, self.age, self.skill)
