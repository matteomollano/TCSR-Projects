from Person import Person

Julian = Person("Julian", "10", "Male", "4'6\"", "Black")
Julian.display()

# changing an object's property/attribute
Julian.setName("Ethan")
print(Julian.getName())
Julian.display()