class Animal:
    def __init__(self, breed, cost):
        self.breed = breed
        self.cost = cost

    def move(self):
        pass


class Fish(Animal):
    def move(self):
        return "Плавает"


class Bird(Animal):
    def move(self):
        return "Летает"


class ZooShop:
    def __init__(self):
        self.animals = []

    def add_animals(self, animal):
        self.animals.append(animal)

    def get_most_expensive_breed(self):
        if not self.animals:
            return None

        most_expensive_animal = max(self.animals, key=lambda x: x.cost)
        return most_expensive_animal.breed

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            for animal in self.animals:
                file.write(f"{animal.breed}, {animal.cost}\n")


if __name__ == "__main__":
    zoo_shop = ZooShop()

    fish1 = Fish("Золотая рыбка", 50)
    fish2 = Fish("Гуппи", 20)

    bird1 = Bird("Попугай", 100)
    bird2 = Bird("Канарейка", 30)

    zoo_shop.add_animals(fish1)
    zoo_shop.add_animals(fish2)
    zoo_shop.add_animals(bird1)
    zoo_shop.add_animals(bird2)

    most_expensive_breed = zoo_shop.get_most_expensive_breed()
    print(f"Самая дорогая порода: {most_expensive_breed}")

    zoo_shop.write_to_file("zoo_data.txt")
