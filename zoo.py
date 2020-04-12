# Create a tuple named zoo that contains 10 of your favorite animals.
zoo = ("okapi", "giraffe", "elephant", "panda", "wolf", "meerkat", "river otter", "peacock", "snow leopard", "gorilla")
# Find one of your animals using the tuple.index(value) syntax on the tuple
print(zoo.index("panda"))
# Determine if an animal is in your tuple by using value in tuple syntax
animal_to_find = "wolf"
if animal_to_find in zoo:
    print(animal_to_find)
# Create a variable for the animals in your zoo tuple, and print them to the console.
(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo
print(sixth_animal)
print(second_animal)
print(first_animal)
# Convert your tuple into a list.
zoo_list = list(zoo)
# Use extend() to add three more animals to your zoo.
zoo_list.extend(["racoon", "lion", "fox"])
# Convert the list back into a tuple
zoo_tuple = tuple(zoo_list)



