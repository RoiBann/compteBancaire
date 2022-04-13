class Compte:

    def __init__(self, numero_compte, nom_proprietaire, solde):
        self.solde = solde
        self._numero_compte = numero_compte
        self._nom_proprietaire = nom_proprietaire


    def retrait(self):
        _montant_retrait = float(input("Entrez le montant du retrait: "))
        if self.solde >= _montant_retrait:
            self.solde -= _montant_retrait
            print("Retrait montant ", _montant_retrait)
        else:
            print("Montant du solde insuffisant.")


    def versement(self):
        virement = float(input("Entrez le montant du virement: "))
        self.solde += virement
        print("Versement déposé: ", virement)

    def solde_dispo(self):
        affichage = ""
        affichage += "Montant disponible : "
        affichage += str(self.solde)
        affichage += " EURO"
        return affichage

    def afficher_solde(self):
        print(self.solde_dispo())

    def get_numero_compte(self):
        return self._numero_compte

    def get_nom_proprietaire(self):
        return self._nom_proprietaire

    def get_solde(self):
        return self.solde

def test_all():

    c = Compte(1234, "Eude", 200)
    c.afficher_solde()
    c.retrait()
    c.afficher_solde()
    c.versement()
    c.afficher_solde()

# test_all()



