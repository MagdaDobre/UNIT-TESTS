from App.cont_page import *

class TestCont:
    def setup_method(self):
        print('Se executa la inceput')
        self.cont = cont('ro12bcr','andrei', 100)

    def teardown_method(self):
        print('Se executa la final')

    def test_afisare_sold(self):
        assert self.cont.afisare_sold() == (f'Titularul andrei are în contul ro12bcr suma de 100 lei.'), 'Atentie, soldul nu este corect!'

    def test_debitare_cont(self):
        self.cont.debitare_cont(50)
        assert self.cont.sold == 50, 'Atentie, suma debitata nu a fost retrasa din cont!'

    def test_creditare_cont(self):
        self.test_debitare_cont()
        self.cont.creditare_cont(150)
        assert self.cont.sold == 200, 'Atentie, suma creditata nu a fost adaugata in cont!'

