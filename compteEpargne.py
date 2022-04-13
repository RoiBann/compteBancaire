from compte import Compte


class CompteEpargne(Compte):

    def __init__(self, pourcentage_interets, numero_compte, nom_proprietaire, solde):
        super().__init__(numero_compte, nom_proprietaire, solde)
        self.pourcentage_interets = pourcentage_interets

    def versementCE(self):
        virement = float(input("Entrez le montant du versement : "))
        print(self.pourcentage_interets)
        self.solde += virement * self.pourcentage_interets
        print("Versement déposé ", virement)
        return virement

    def montant_dispo(self):
        affichageCE = ""
        affichageCE += "Montant disponible :"
        affichageCE += str(self.solde)
        affichageCE += "€"
        return affichageCE

    def solde_ce(self):
        print(self.montant_dispo())

    def appliquer_interets(self):
        print(self._nom_proprietaire)
        self._nom_proprietaire = 'test'
        print(self._nom_proprietaire)
        print("Versement plus interêts obtenus ", self.set_pourcentage_interets(), "€")

    def get_pourcentage_interets(self):
        return self.pourcentage_interets

    def set_pourcentage_interets(self):
        for i in range(1):
            pourcentage_interets = str(self.versementCE() * 1.02)
            return pourcentage_interets

    def get_nom_proprietaire(self):
        return self._nom_proprietaire

    def set_nom_proprietaire(self):
        return self._nom_proprietaire




def test_all_ce():
    name = input("entrez un nom : ")
    ce = CompteEpargne(1.02, 5678, name, 1000)
    ce.versementCE()
    ce.afficher_solde()
    print(ce.get_nom_proprietaire())

# test_all_ce()



