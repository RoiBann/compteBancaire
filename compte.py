class Compte:

    def __init__(self, numero_compte, nom_proprietaire, solde):
        self._numero_compte = numero_compte
        self._nom_proprietaire = nom_proprietaire
        self._solde = solde

    def retrait(self):


    def versement(self):


    def afficher_solde(self):

    def get_numero_compte(self):
        return self._numero_compte

    def get_nom_proprietaire(self):
        return self._nom_proprietaire

    def get_solde(self):
        return self._solde