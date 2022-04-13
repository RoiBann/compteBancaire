from compte import Compte


class CompteCourant(Compte):

    def __init__(self, autorisation_decouvert, pourcentage_agios, numero_compte, nom_proprietaire, solde):
        super().__init__(numero_compte, nom_proprietaire, solde)
        self._autorisation_decouvert = autorisation_decouvert
        self._pourcentage_agios = pourcentage_agios


    def retrait(self):
        montant_retrait = float(input("Entrez le montant du retrait : "))
        if self.solde >= montant_retrait:
            self.solde -= montant_retrait
            print("Montant du retrait effectué : ", montant_retrait)
        elif montant_retrait > self._autorisation_decouvert:
            print("Plafond découvert atteint.")
            recommencer = input("Souhaitez-vous entrez un nouveau montant? (y/n) :")
            while recommencer == 'y':
                self.retrait()
                break
            else:
                print("Au revoir")
        else:
            print('je passe dans le else')
            # agios = montant_retrait / self._pourcentage_agios
            self.appliquer_agios()
            print("Solde avec agios : ", self.appliquer_agios())


    def versementCC(self):
        virement = float(input("Entrez le montant du versement : "))
        self.solde += virement
        print("Montant déposé : ", virement)
        return virement


    def appliquer_agios(self):
        print("entrer appliquer agios")
        agios = self.solde / self._pourcentage_agios
        return agios

    def get_autorisation_decouvert(self):
        return self._autorisation_decouvert

    def get_pourcentage_agios(self):
        return self._pourcentage_agios

    def set_appliquer_agios(self):
        if self.solde < 0:
            self.appliquer_agios()


    def set_autorisation_decouvert(self):
        pass


    def set_pourcentage_agios(self):
        return self._pourcentage_agios

def test_all_cc():
    name = input("Entrez votre nom : ")
    cc = CompteCourant(-500, 1.02, 1357, name, 1300)
    cc.afficher_solde()
    cc.retrait()
    cc.afficher_solde()
    cc.versementCC()
    cc.afficher_solde()

test_all_cc()



