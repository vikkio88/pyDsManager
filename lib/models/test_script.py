from lib.generator.randomfiller import RandomFiller
from lib.models import Module
from lib.models import Match


def print_menu():
    print('1 . Generate and print team')
    print('2 . Generate and print player')
    print('3 . Generate two teams and simulate few games')
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
            print(team.get_players_by_role('GK'))
            print(team.get_best_player_by_role('GK'))
        if command == '2':
            player = rnd.get_player(rnd.get_locale())
            print(player, player.nationality, player.role)
        if command == '3':
            t1 = rnd.get_team()
            t2 = rnd.get_team()
            wa = 0
            wh = 0
            d = 0
            for i in range(100):
                m = Match(t1, t2)
                result = m.simulate()
                print("{}.\t {}".format(str(i), result))
                if result.goalHome > result.goalAway:
                    wh += 1
                elif result.goalAway > result.goalHome:
                    wa += 1
                else:
                    d += 1
            print("{} ({}) win percentage: {}%".format(t1.name, t1.get_avg_skill(), wh))
            print("{} ({}) win percentage: {}%".format(t2.name, t2.get_avg_skill(), wa))
            print("teams skill diff {}".format(round(abs(t1.get_avg_skill() - t2.get_avg_skill())), 2))
            print("teams drawn {} times".format(d))


if __name__ == '__main__':
    main()
