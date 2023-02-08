from App.dreptunghi_page import *

class TestDreptunghi:

    def setup_method(self):
        print('Se executa la inceput')
        self.dreptunghi = dreptunghi(4, 5, 'verde')
        self.culoare_noua = [4, 5, 'albastru']

    def teardown_method(self):
        print('Se executa la final')

    def test_descrie(self):
        assert self.dreptunghi.descrie() == (4, 5, 'verde'), 'Atentie, descrierea nu este cea setata!'

    def test_aria(self):
        assert self.dreptunghi.aria() == 20, 'Atentie, aria nu este corecta!'

    def test_perimetrul(self):
        assert self.dreptunghi.perimetrul() == 18, 'Atentie, perimetrul nu este corect!'

    def test_schimba_culoare(self):
        self.dreptunghi.schimba_culoarea('albastru')
        assert self.dreptunghi.culoare == 'albastru', 'Atentie, culoarea nu s-a schimbat. Verificati metoda.'
        assert self.dreptunghi.descrie() == (4, 5, 'albastru'), 'Atentie, culoarea nu s-a schimbat.'
