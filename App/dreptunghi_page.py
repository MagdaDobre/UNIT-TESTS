
class dreptunghi:

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        self_descrie = (self.lungime, self.latime, self.culoare)
        return self_descrie
        print(f'Dreptunghiul are lungimea de {self.lungime}, latimea de {self.latime} si culoarea {self.culoare}.')

    def aria(self):
        return self.lungime * self.latime

    def perimetrul(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare
