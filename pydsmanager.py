from lib.generator import RandomFiller
from lib.lazyassconsole import Console
from lib.config.modules import modules
from lib.config.locales import locales

if __name__ == '__main__':

    rnd = RandomFiller()
    team = rnd.get_team(rnd.get_locale())

    print(team.name)
    print(team.nationality)
    for player in team.players:
        print(player)
