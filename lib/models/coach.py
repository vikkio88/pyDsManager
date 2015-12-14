from lib.models import Person


class Coach(Person):
    module = ""

    def __init__(self, person=Person()):
        self.name = person.name
        self.surname = person.surname
        self.skill = person.skill

