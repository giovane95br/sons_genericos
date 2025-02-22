class Animal:
    def __init__(self, motivo=""):
        self.motivo = motivo

    def fazer_som(self):
        return "Algum som genérico"

class Copo(Animal):
    def fazer_som(self):
        return "Copo caindo"

class Cachorro(Animal):
    def fazer_som(self):
        return f"🐶 Cachorro latindo porque {self.motivo}"

class Gato(Animal):
    def fazer_som(self):
        return f"🐱 Gato miando porque {self.motivo}"


copo = Copo()
cachorro = Cachorro(motivo="se assustou com o copo caindo")
gato = Gato(motivo="ouviu o cachorro latindo")

animais = [copo, cachorro, gato]

for animal in animais:
    print(f'\n{animal.fazer_som()}')
