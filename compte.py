from abc import ABC, abstractmethod

class Compte(ABC):

    @abstractmethod
    def __init__(self, numero_compte, nom_proprietaire, solde):
        self.solde = solde
        self._numero_compte = numero_compte
        self._nom_proprietaire = nom_proprietaire
        self._autorisation_decouvert = 0


    def retrait(self, _montant_retrait):
        """
        Fonction retrait.
        Si le retrait est supérieur au solde, un message d'erreur s'affiche
        Enlève le montant donné du compte.
        """
        if _montant_retrait <= self._autorisation_decouvert + self.solde:
            self.solde -= _montant_retrait
            print("Retrait montant ", _montant_retrait)
        else:
            raise Exception("Montant indisponible")


    def versement(self, virement):
        """
        Fonction de dépot sur le compte
        """
        self.solde += virement
        print("Versement déposé: ", virement)


    def solde_dispo(self):
        """
        Fonction permettant d'afficher le solde disponible
        """
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




if __name__ == "__main__":
    def test_all():
        c = Compte(1234, "Eude", 200)
        c.afficher_solde()
        c.retrait(250)
        c.afficher_solde()
        c.versement(50)
        c.afficher_solde()


    test_all()



