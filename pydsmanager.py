from faker import Faker

if __name__ == '__main__':
    print("Here you go")

faker = Faker('it_IT')

print(faker.name())

