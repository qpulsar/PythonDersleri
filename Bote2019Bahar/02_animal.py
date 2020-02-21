class Animal:
    def __init__(self, renk, ayak):
        self.renk = renk
        self.ayak = ayak

    def sesver(self):
        print("Sessizlik")

class Dog(Animal):
    def sesver(self):
        print("Hav Hav")


a = Animal("gri", 9)
print(a.ayak)
a.sesver()
b = Dog("Kahverengi", 4)
print(b.ayak, b.renk)
