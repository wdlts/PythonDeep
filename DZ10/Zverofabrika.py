from DZ.DZ10.Cat import Cat
from DZ.DZ10.Dog import Dog

class ZveroFabrika:
    def new_animal(self, animal_type, name, breed, age):
        if animal_type.lower() == "cat":
            return Cat(name, breed, age)
        elif animal_type.lower() == "dog":
            return Dog(name, breed, age)
        else:
            raise ValueError("Invalid animal type")

fabrika = ZveroFabrika()

cat = fabrika.new_animal("cat", "Fluffy", "Persian", 3)
dog = fabrika.new_animal("dog", "Buddy", "Golden Retriever", 5)

print(cat.say())
print(dog.say())