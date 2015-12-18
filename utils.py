from gameconfig import config


def print_banner():
    print(config['banner'])


def print_menu():
    for menu_entry in config['menu_choice']:
        print("{} . {}".format(menu_entry, config['menu_choice'][menu_entry]))


def check_cmd(cmd):
    if cmd in config['menu_choice']:
        print(config['menu_choice'][cmd])
