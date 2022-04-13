from compte import Compte


class CompteCourant(Compte):

    def __init__(self, autorisation_decouvert, pourcentage_agios, numero_compte, nom_proprietaire, solde):
        super().__init__(numero_compte, nom_proprietaire, solde)
        self._autorisation_decouvert = autorisation_decouvert
        self._pourcentage_agios = pourcentage_agios


    def retrait(self, montant_retrait):
        """
        Fonction de retrait d'argent.
        Si le compte passe en négatif, des agios sont appliqués
        """
        #### GESTION ERREURS #####
        if type(montant_retrait) is str:
            return
        #### ACTIONS #####
        try:
            super().retrait(montant_retrait)
            self.set_appliquer_agios()
        except Exception as e:
            print(e)


    def versement(self, virement):
        self.solde += virement
        print("Montant déposé : ", virement)
        return virement


    def appliquer_agios(self):
        agios = self.solde / self._pourcentage_agios
        return agios


    def get_autorisation_decouvert(self):
        return self._autorisation_decouvert


    def get_pourcentage_agios(self):
        return self._pourcentage_agios


    def set_appliquer_agios(self):
        if self.solde < 0:
            self.solde += self.appliquer_agios()


    def set_autorisation_decouvert(self):
        pass


    def set_pourcentage_agios(self):
        return self._pourcentage_agios


if __name__ == '__main__':
    def test_all_cc():
        # name = input("Entrez votre nom : ")
        cc = CompteCourant(500, 1.02, 1357, "name", 1300)
        cc.afficher_solde()
        cc.retrait(1300)
        cc.afficher_solde()
        cc.retrait(100)
        cc.afficher_solde()
        cc.versement(50)
        cc.afficher_solde()
        cc.retrait(500)
        cc.afficher_solde()
        cc.retrait(900)
        cc.afficher_solde()
        cc.retrait(11.1)
        cc.afficher_solde()
        cc.retrait('a')


    test_all_cc()
