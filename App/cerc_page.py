
class circle:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare


    def descrie_cerc(self):
        self_descrie = (self.raza, self.culoare)
        return self_descrie

    def aria(self):
        return self.raza * self.raza * 3.14

    def diametru(self):
        return self.raza + self.raza

    def circumferinta(self):
        return (self.raza + self.raza) * 3.14