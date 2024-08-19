class Zoo:
    __animal = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animal += 1

    def get_info(self, species):
        if species == "mammal":
            total_animals = [element for element in self.mammals]
            Species = "Mammals"
        elif species == "fish":
            total_animals = [element for element in self.fishes]
            Species = "Fishes"
        else:
            total_animals = [element for element in self.birds]
            Species = "Birds"

        return f"{Species} in {self.name}: {', '.join(total_animals)}\nTotal animals: {Zoo.__animal}"


name_of_the_zoo = input()
number_of_lines = int(input())

zoo = Zoo(name_of_the_zoo)

for current_line in range(number_of_lines):
    animal_info = input().split()
    species = animal_info[0]
    name = animal_info[1]
    zoo.add_animal(species, name)

info_for_species = input()

print(zoo.get_info(info_for_species))

