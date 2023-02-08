from App.cerc_page import *

class TestCircle:

    def setup_method(self):
        print('Se executa la inceput')
        self.cerc = circle(5,'alb')
        self.culoare = (5,'alb')

    def teardown_method(self):
        print('Se executa la final')

    def test_descrie(self):
        assert self.cerc.descrie_cerc() == (5,'alb'), 'Atentie, descrierea nu este cea setata!'

    def test_aria(self):
        assert self.cerc.aria() == 78.5, 'Atentie, aria nu este corecta!'

    def test_diametru(self):
        assert self.cerc.diametru() == 10, 'Atentie, diametru nu este corect!'

    def test_circumferinta(self):
        assert self.cerc.circumferinta() == 31.400000000000002, 'Atentie, circumferinta nu este corecta!'

