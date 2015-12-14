from lib.generator import Randomizer
from lib.lazyassconsole import Console
from lib.config.modules import modules

if __name__ == '__main__':
    for module in modules:
        Console.print(module['name'], 'r')

    r = 100
    max_diff = 0

    for p in range(0, 110, 10):
        t = 0
        f = 0
        Console.print("Testing " + str(p) + "% ...", 'b')
        for i in range(r):
            if Randomizer.bool_on_percentage(p):
                t += 1
            else:
                f += 1
        Console.print("Results for " + str(p) + "%", 'p', 'u')
        Console.print("trues: " + str(t) + "/" + str(r), 'g', 'b')
        Console.print("false: " + str(f) + "/" + str(r), 'r', 'b')
        diff = abs(p - t)
        if diff > max_diff:
            max_diff = diff
        Console.print("diff: " + str(diff), 'y')
    print()
    Console.print("Max diff: " + str(max_diff), "r", "b")
