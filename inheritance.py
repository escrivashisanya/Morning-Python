#Parenmt class/Super class/Base class
class Animal :
    isMammal = True

    def speak(self):
        print("Animal is speaking")

    def move(self):
        print("Animal is moving")

#Child class/Sub class/Derived class
class Cat(Animal) :
    def sound(self):
        print("Cat is meowing")

    def climb(self):
        print("Cat is climbing a tree")


class Horse :
    def neigh(self):
        hasTail = True

        print("Horse is neighing")




a = Animal()




c = Cat()
c.



h = Horse()