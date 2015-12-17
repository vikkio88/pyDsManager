from lib.generator import RandomFiller
from lib.lazyassconsole import Console
from lib.config.modules import modules
from lib.config.locales import locales
from lib.models import Module


def print_menu():
    print('1 . Generate and print team')
    print('2 . Generate and print player')
    print('q. Quit')


def main():
    rnd = RandomFiller()
    command = ''
    while command != 'q':
        print_menu()
        command = input()
        if command == '1':
            team = rnd.get_team()
            print(team.name)
            print(team.nationality)
            print(team.coach, team.coach.module)
            m = Module(team.coach.module)
            if m.is_balanced():
                print("balanced")
            elif m.is_defensive():
                print("defensive")
            else:
                print("offensive")
            print("Players per role")
            print(team.get_players_per_role())
            print("Roles needed by {}".format(m.name))
            print(m.get_roles_needed())
            if not m.is_applicable_to_team(team):
                print("module not applicable, missing:")
                print(m.roles_missing_team(team))
            else:
                print("{} is applicable".format(m.name))
        if command == '2':
            player = rnd.get_player(rnd.get_locale())
            print(player, player.nationality, player.role)


if __name__ == '__main__':
    main()
