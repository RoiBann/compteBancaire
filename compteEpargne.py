from compte import Compte


class CompteEpargne(Compte):

    def __init__(self, pourcentage_interets, numero_compte, nom_proprietaire, solde):
        super().__init__(numero_compte, nom_proprietaire, solde)
        self.pourcentage_interets = pourcentage_interets


    def versement(self, virement):
        """
        Fonction de dépot sur le compte avec ajout des interêts
        """
        print(self.pourcentage_interets)
        self.solde += virement * self.pourcentage_interets
        print("Versement déposé ", virement)
        return virement

    def montant_dispo(self):
        affichageCE = "Montant disponible :"
        affichageCE += str(self.solde)
        affichageCE += "€"
        return affichageCE

    def solde(self):
        print(self.montant_dispo)


    def get_pourcentage_interets(self):
        return self.pourcentage_interets


    def get_nom_proprietaire(self):
        return self._nom_proprietaire


    def set_nom_proprietaire(self):
        return self._nom_proprietaire


if __name__ == '__main__':
    def test_all_ce():
        ce = CompteEpargne(1.02, 5678, "name", 1000)
        ce.versement(50)
        ce.afficher_solde()
        ce.retrait(250)
        ce.afficher_solde()
        print(ce.get_nom_proprietaire())


    test_all_ce()
