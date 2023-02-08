
class cont:

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        return (f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei.')

    def debitare_cont(self,suma):
        if suma > self.sold:
            print(f'Suma solicitata depaseste soldul actual in valoare de {self.sold} lei.')
        else:
            self.sold = self.sold - suma
            print(f'Ati retras suma de {suma} lei. Soldul actual este de {self.sold} lei.')

    def creditare_cont(self, suma):
        self.sold = self.sold + suma
        print(f'Ati alimentat contul cu suma de {suma} lei. Soldul actual este de {self.sold} lei.')