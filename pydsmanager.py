from lib.generator import RandomFiller

if __name__ == '__main__':
    print("Here you go some coaches")
    for _ in range(20):
        rnd = RandomFiller()
        pl = rnd.get_coach()
        print(pl)
    print("\n\nHere you go some players")
    for _ in range(20):
        rnd = RandomFiller()
        pl = rnd.get_player()
        print(pl)
