from lib.generator import RandomFiller
from lib.lazyassconsole import Console

if __name__ == '__main__':
    print("ciao")
    Console.print_red("ciao")
    Console.print_blue("ciao")
    Console.print_pink("ciao")
    rnd = RandomFiller()
    pl = rnd.get_coach()
    Console.print(pl)

    """
    print("Here you go some coaches")
    for _ in range(20):
        rnd = RandomFiller()
        pl = rnd.get_coach()
        print(pl)
    print("\n\nHere you go some players")
    for _ in range(20):
        rnd = RandomFiller()
        pl = rnd.get_player()
        Console.print(pl.__str__(), 1)
    """
