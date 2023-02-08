from App.angajat_page import *

class TestAngajat():
    def setup_method(self):
        print('Se executa la inceput')
        self.angajat = angajat('Andrei','Vlad', 5000)

    def teardown_method(self):
        print('Se executa la final')

    def test_descriere(self):
        assert self.angajat.descrie() == ('Angajatul se numeste Andrei Vlad si are salariul de 5000 de lei.'), 'Error, descrierea nu functioneaza corect!'

    def test_nume_complet(self):
        assert self.angajat.nume_complet() == 'Andrei Vlad', 'Error, numele complet nu este corect!'

    def test_salariu_lunar(self):
        assert self.angajat.salariu_lunar() == 5000, 'Error, salariul lunar nu corespunde.'

    def test_salariu_anual(self):
        assert self.angajat.salariu_anual() == 60000, 'Error, calculul salariului anual nu este corect.'

    def test_marire_salariu(self):
        self.angajat.marire_salariu(30)
        assert self.angajat.salariu == 6500, 'Error, calculul salarial nu a fost efectuat corect'
        assert self.angajat.descrie() == ('Angajatul se numeste Andrei Vlad si are salariul de 6500.0 de lei.'), 'Error, marirea salariala nu a fost efectuata corect'