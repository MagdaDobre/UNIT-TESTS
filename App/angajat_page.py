
class angajat:
    nume = None
    prenume = None
    salariu = 0

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        return (f'Angajatul se numeste {self.nume} {self.prenume} si are salariul de {self.salariu} de lei.')

    def nume_complet(self):
        return self.nume + ' ' + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.salariu = self.salariu + (self.salariu * procent / 100)