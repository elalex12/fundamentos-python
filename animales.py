class animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("el animal hace un sonido")


class Perro(animal):
    def hablar(self):
        print(f"{self.nombre} dice ¡Guau!")
perro = Perro("firulais")
perro.hablar()


class Gato(animal):
    def hablar (self):
        print(f"{self.nombre} dice : miau")

animales = [Perro("Boby"),Gato("Michi")]

for animal in animales:
    animal.hablar()