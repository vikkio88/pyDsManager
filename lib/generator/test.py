from lib.generator import Randomizer

if __name__ == '__main__':
    r = 100
    max_diff = 0

    for p in range(0, 110, 10):
        t = 0
        f = 0
        print("--Testing " + str(p) + "% ...")
        for i in range(r):
            if Randomizer.bool_on_percentage(p):
                t += 1
            else:
                f += 1
        print("--Results for " + str(p) + "%")
        print("trues: " + str(t) + "/" + str(r))
        print("false: " + str(f) + "/" + str(r))
        diff = abs(p - t)
        if diff > max_diff:
            max_diff = diff
        print("diff: " + str(diff))
        print()
    print()
    print("--Max diff: " + str(max_diff))
