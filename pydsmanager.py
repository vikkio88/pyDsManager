from lib.generator import RandomFiller

if __name__ == '__main__':
    print("Here you go")
for _ in range(20):
    rnd = RandomFiller()
    pl = rnd.get_coach()
    print(pl.name)
    print(pl.surname)
    print(pl.age)
    print(pl.skill)
    print('-------\n')
