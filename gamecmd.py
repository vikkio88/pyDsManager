from cmd import Cmd
import utils
from lib.lazyassconsole import Console


class GameCmd(Cmd):
    prompt = '\n> '

    def default(self, line):
        Console.print('Invalid command, type "help" for a list of commands')

    def do_quit(self, arg):
        return True

    def do_show(self, arg):
        if arg == 'teams' or arg == 't':
            utils.show_teams()
        elif arg == 'players' or arg == 'p':
            utils.show_free_players()
        else:
            self.default()

    def do_generate(self, arg):
        if arg == 'teams' or arg == 't':
            utils.generate_team()
        elif arg == 'players' or arg == 'p':
            utils.generate_player()
